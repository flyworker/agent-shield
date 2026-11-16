import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from unittest import mock

import server


class ScanLimitsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join(timeout=5)
        cls.server.server_close()

    def _post(self, body):
        req = urllib.request.Request(
            self.base + "/api/scan",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.status, json.loads(resp.read())
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read())

    def test_invalid_json_returns_400(self):
        with mock.patch("server.run_pipeline") as rp:
            code, body = self._post(b"{not valid json")
        self.assertEqual(code, 400)
        self.assertEqual(body, {"error": "invalid json"})
        rp.assert_not_called()

    def test_prompt_too_long_returns_413(self):
        with mock.patch("server.run_pipeline") as rp:
            prompt = "a" * (server.MAX_PROMPT_CHARS + 1)
            body = json.dumps({"prompt": prompt}).encode()
            code, resp = self._post(body)
        self.assertEqual(code, 413)
        self.assertEqual(resp, {"error": "prompt too long", "max": server.MAX_PROMPT_CHARS})
        rp.assert_not_called()


if __name__ == "__main__":
    unittest.main()
