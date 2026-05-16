FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install nanobot-ai mcp --no-cache-dir

COPY config.json /app/config.json
COPY mcp_servers/ /app/mcp_servers/
COPY workspace/ /app/workspace/

RUN mkdir -p /app/data /app/workspace/memory

EXPOSE 18790

CMD ["nanobot", "gateway"]