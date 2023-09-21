FROM python:3.8

RUN apt-get update && apt-get install -y \
    python3-pip

COPY . .

WORKDIR .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir fastapi uvicorn httpx python-dotenv openai

ENTRYPOINT ["sh", "entry.sh"]
