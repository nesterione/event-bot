FROM python:3.5.2-alpine

COPY req.txt /tmp/

RUN pip3 install --no-cache-dir --disable-pip-version-check -r /tmp/req.txt

RUN mkdir /usr/events-api/
COPY . /usr/events-api/
WORKDIR /usr/events-api/

EXPOSE 6910

CMD ["python3", "-u", "app.py"]
