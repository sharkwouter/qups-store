FROM python:3.7-alpine

RUN adduser -D qups

WORKDIR /home/qups

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY .flaskenv .flaskenv
COPY app app
COPY qups-store.py config.py ./
USER qups
RUN python -m flask db init && python -m flask db migrate && python -m flask db upgrade


EXPOSE 5000
CMD python -m flask run --host=0.0.0.0
