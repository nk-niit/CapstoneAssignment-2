FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /capstone

COPY requirements.txt /capstone/

WORKDIR /capstone

RUN pip install -r requirements.txt

COPY . /capstone/