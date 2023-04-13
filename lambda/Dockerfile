FROM python:3.9-slim
# FROM python:3.9

RUN pip3 install --upgrade pip

RUN pip3 install aws-sam-cli

RUN apt-get update

RUN apt-get install unzip

WORKDIR /app

CMD ["python3"]
