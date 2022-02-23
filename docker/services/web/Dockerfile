# syntax=docker/dockerfile:1
FROM python:3.10-alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /jakdojade
COPY ../../../requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY docker/web .
EXPOSE 5000
WORKDIR /jakdojade/services/web
CMD ["flask", "run"]
