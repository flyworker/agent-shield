FROM python:3.12-slim

WORKDIR /app

# System deps for onnxruntime (forcefield[ml])
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 curl \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir 'forcefield[ml]==0.7.4'

COPY server.py shieldprompt.html ./

# Cloud Run injects $PORT; server.py already honors it.
ENV BIND_HOST=0.0.0.0
ENV PORT=8080
EXPOSE 8080

CMD ["python3", "server.py"]
