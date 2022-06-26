FROM python:3.9-alpine

ENV PYTHONUNBUFFERD=1
WORKDIR /logic

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . /logic/

EXPOSE 8000