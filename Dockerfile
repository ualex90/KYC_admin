FROM python:3.11-slim

WORKDIR /code
COPY pyproject.toml .
COPY poetry.lock .
COPY scripts/create_user.sh .
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . .
