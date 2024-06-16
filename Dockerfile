FROM python:3.10-slim

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--no-access-log]