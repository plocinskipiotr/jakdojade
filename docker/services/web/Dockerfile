# syntax=docker/dockerfile:1
FROM python:3.10-alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1
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
EXPOSE 5000
CMD ["flask", "run", "--no-reload"]
