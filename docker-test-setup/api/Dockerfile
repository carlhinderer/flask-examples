FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

ENV PIP_ROOT_USER_ACTION=ignore
RUN python -m venv venv
RUN . venv/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src src

ENV FLASK_APP src/app.py
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]