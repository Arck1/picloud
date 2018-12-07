FROM python:3.5
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
