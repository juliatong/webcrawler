# syntax = docker/dockerfile:1.4

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /code
COPY ./requirements.txt /code

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code

FROM builder as dev-envs

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# CMD ["python", "hello.py"]
