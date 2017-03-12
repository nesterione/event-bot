# coding: utf-8
# !flenv/bin/python
from app import app
import os

if __name__ == '__main__':
    try:
        base_url = os.environ['BASE_URL']
        events_user = os.environ['EVENTS_USER']
        events_pass = os.environ['EVENTS_PASS']
        api_token = os.environ['API_TOKEN']
    except Exception as ex:
        base_url = 'http://localhost:6910'
        events_user = 'admin'
        events_pass = 'admin'
        api_token = '123'
        print("Not set BASE_URL, EVENTS_PASS or EVENTS_USER environment variables, will use default values")

    app.config['BASE_URL'] = base_url
    app.config['EVENTS_USER'] = events_user
    app.config['EVENTS_PASS'] = events_pass
    app.config['API_TOKEN'] = api_token
    app.run(debug=True, host="0.0.0.0", port=9231)
