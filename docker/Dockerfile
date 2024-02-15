FROM python:3.12-slim

RUN pip install poetry

COPY ../pyproject.toml ../poetry.lock ./
RUN poetry install --no-root

COPY .. .
EXPOSE 5000

WORKDIR src/
CMD ["poetry", "run", "python", "main.py"]
