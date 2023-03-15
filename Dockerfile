FROM python:3.9

RUN pip3 install --upgrade pip

WORKDIR /app

CMD ["python3"]
