# Dockerfile - formula-predictions-backend
# =======================================================
# Formula Predictions backend application.

FROM python:3.13.5-alpine3.22

RUN apk add --no-cache curl

WORKDIR /app/src
COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . .
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl --fail http://localhost:8000/health/ || exit 1

CMD ["uvicorn", "--app-dir", "./src", "main:app", "--host", "0.0.0.0", "--port", "8000"]
