FROM python:3.11-slim

WORKDIR /app

ARG APP_ENV_ARG=production
ENV APP_ENV=${APP_ENV_ARG}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

CMD ["python", "src/app.py"]
