FROM localstack/localstack:latest

COPY table_setup.py ./

COPY s3_setup.py ./

RUN aws configure set region ap-northeast-1

RUN aws configure set aws_access_key_id dummy

RUN aws configure set aws_secret_access_key dummy

# RUN python3 table_setup.py

# ENTRYPOINT [ "python3","table_setup.py" ]