FROM python:3.11-slim
WORKDIR /app

COPY reqmest.txt .
RUN pip install --no-cache-dir -r reqmest.txt
COPY app.py .

RUN useradd -m -u 1001 appuser
USER appuser

CMD ["python", "app.py"]