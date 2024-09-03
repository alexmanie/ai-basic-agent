FROM python:3.11

ENV CONTAINER_HOME=/var/www

WORKDIR $CONTAINER_HOME
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "backend:app"]