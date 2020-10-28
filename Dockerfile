FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /capstone

WORKDIR /capstone

COPY . /capstone/

RUN pip install -r requirements.txt