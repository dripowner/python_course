FROM ubuntu:22.04

USER root

RUN apt update -y

RUN apt-get install -y texlive-latex-base python3.11 python3-pip

WORKDIR /hw2

RUN mkdir artifacts

COPY 2.py 2.py

COPY img.jpg img.jpg

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN python3 2.py

