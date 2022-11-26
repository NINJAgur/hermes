FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt