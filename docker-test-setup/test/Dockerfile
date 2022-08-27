FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

ENV PIP_ROOT_USER_ACTION=ignore
RUN python -m venv venv
RUN . venv/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY tests tests

CMD pytest