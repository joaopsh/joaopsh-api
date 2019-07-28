FROM python:3.7-alpine

RUN apk update && \
    apk add postgresql-dev \
            gcc \
            musl-dev

WORKDIR /usr/src/app

RUN pip install pipenv
RUN pipenv --python 3.7

COPY Pipfile.lock .
RUN pipenv install --deploy --ignore-pipfile

COPY . .

ENTRYPOINT pipenv run python app.py