FROM python:3.9-buster

RUN pip install poetry==1.8.0

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "app.web:app", "--host", "0.0.0.0", "--port", "8000"]
