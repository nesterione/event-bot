# coding: utf-8
#!flenv/bin/python
from app import app

# TODO add env variable for app location

app.config['BASE_URL'] = "http://api.events.nesterione.com"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9231)