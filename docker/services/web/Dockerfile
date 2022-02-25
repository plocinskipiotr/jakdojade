# syntax=docker/dockerfile:1
FROM python:3.10-alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /jakdojade
COPY . .
COPY requirements.txt requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk update --no-cache \
&& apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
&& pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& apk del .build-deps
RUN apk add postgresql-libs libpq --no-cache
#WORKDIR /jakdojade
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
EXPOSE 5000
WORKDIR /jakdojade/services/web
CMD ["flask", "run"]
