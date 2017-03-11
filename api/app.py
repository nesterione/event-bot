#!flenv/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, g
from pymongo import MongoClient
from dataservice import DataService
import json
from bson import ObjectId
# from bson.json_util import dumps
import os
import datetime
from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, ObjectId):
                return str(obj)
            if isinstance(obj, datetime.datetime):
                return obj.timestamp()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)



# TODO refactor architecture

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.json_encoder = CustomJSONEncoder

@app.route('/')
def index():
    return "Hi, this is Events API <br> /api/v0.1/events - return all events"


@app.route('/api/v0.1/events', methods=['GET'])
def get_events():
    service = DataService(get_db())
    cursor = service.get_actual_events()
    events = [event for event in cursor]
    return  jsonify(events)


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'mongo_client'):
        db_uri = os.environ['DB_URI']

        client = MongoClient(db_uri)
        g.mongo_client = client

    db_name = os.environ['DB_NAME']
    return g.mongo_client[db_name]


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'mongo_client'):
        g.mongo_client.close()


if __name__ == '__main__':

    # validate environment variables
    try:
        db_uri = os.environ['DB_URI']
        db_name = os.environ['DB_NAME']
    except Exception as ex:
        print("Not set DB_URI or DB_NAME environment variables")
        raise ex

    app.run(debug=True, host="0.0.0.0", port=6910)