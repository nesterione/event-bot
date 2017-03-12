FROM python:3.5.2-alpine

COPY req.txt /tmp/

RUN pip3 install --no-cache-dir --disable-pip-version-check -r /tmp/req.txt

RUN mkdir /usr/web-client/
COPY . /usr/web-client/
WORKDIR /usr/web-client/

EXPOSE 9231

CMD ["python3", "-u", "run.py"]
