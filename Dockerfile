FROM amazonlinux:2

RUN yum -y update

RUN yum install -y python3

RUN yum install -y zip

WORKDIR /mnt