FROM python:3.13.5-alpine3.22

WORKDIR /app

COPY ./src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
