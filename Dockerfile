FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY rss_download.py ./

CMD [ "python", "./rss_download.py" ]
