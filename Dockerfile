FROM python:3.5.2-alpine

RUN pip3 install flask flask-uploads

WORKDIR /app
ADD . /app/

EXPOSE 5000

VOLUME /app/uploads
ENV FLASK_APP=filedrop.py
CMD flask run --host=0.0.0.0

