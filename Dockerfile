FROM python:3.8

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /usr/src