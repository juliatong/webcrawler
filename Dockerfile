# syntax = docker/dockerfile:1.4

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /code
COPY requirements.txt /code

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY . .

FROM builder as dev-envs

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
# ENTRYPOINT ["python"]
CMD ["python", "hello.py"]
