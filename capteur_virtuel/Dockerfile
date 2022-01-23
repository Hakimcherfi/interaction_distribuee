FROM python

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

CMD ["python","capteur_virtuel.py"]