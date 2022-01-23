FROM python

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

CMD ["mongodb"]