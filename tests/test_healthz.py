import json
import sys
import threading
import unittest
import urllib.request
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import server


class HealthzTest(unittest.TestCase):
    def setUp(self):
        self.original_api_key = server.API_KEY
        self.secret = "dummy-healthz-secret"
        server.API_KEY = self.secret
        self.httpd = server.ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join()
        server.API_KEY = self.original_api_key

    def test_healthz(self):
        host, port = self.httpd.server_address
        with urllib.request.urlopen(f"http://{host}:{port}/healthz") as response:
            body = response.read()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers.get_content_type(), "application/json")

        payload = json.loads(body)
        self.assertEqual(set(payload), {"status", "forcefield", "llm_configured"})
        self.assertIsInstance(payload["status"], str)
        self.assertIsInstance(payload["forcefield"], bool)
        self.assertIsInstance(payload["llm_configured"], bool)
        self.assertEqual(payload["status"], "ok")
        self.assertTrue(payload["llm_configured"])
        self.assertNotIn(self.secret.encode(), body)


if __name__ == "__main__":
    unittest.main()
