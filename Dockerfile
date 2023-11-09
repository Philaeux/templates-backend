FROM python:3.12-slim


COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

WORKDIR src/

CMD ["python3", "main.py"]
