FROM python:3.7-alpine

RUN mkdir -p /surf_bot

WORKDIR /surf_bot

ADD . /surf_bot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "--ini", "wsgi.ini"]
