# coding: utf-8
#!flenv/bin/python
from app import app

# TODO add env variable for app location

#     "http://api.events.nesterione.com"
app.config['BASE_URL'] = "http://localhost:6910"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9231)