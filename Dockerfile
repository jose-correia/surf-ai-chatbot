FROM python:3.7-alpine

RUN mkdir -p /home/menesesjmmc/surf_bot

WORKDIR /home/menesesjmmc/surf_bot

ADD . /home/menesesjmmc/surf_bot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "--ini", "wsgi.ini"]