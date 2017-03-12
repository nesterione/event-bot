#!flenv/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, g, request, abort
from pymongo import MongoClient
from dataservice import DataService
from bson import ObjectId
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
    return jsonify(events)


@app.route('/api/v0.1/events', methods=['PUT'])
def put_event():
    if not request.json:
        abort(400)

    service = DataService(get_db())
    result = service.upsert_event(request.json)
    return jsonify(result), 201


@app.route('/api/v0.1/events/<string:event_id>', methods=['GET'])
def get_event(event_id):
    service = DataService(get_db())
    event = service.get_event(event_id)
    return jsonify(event)


@app.route('/api/v0.1/events/<string:event_id>', methods=['DELETE'])
def delete_event(event_id):
    service = DataService(get_db())
    service.disable_event(event_id)
    return jsonify(event_id), 201


@app.route('/api/v0.1/events/<string:event_id>/attendees', methods=['PUT'])
def put_attendee(event_id):
    if not request.json:
        abort(400)

    service = DataService(get_db())
    result = service.upsert_attendee(event_id, request.json)
    return jsonify(result), 201


@app.route('/api/v0.1/events/<string:event_id>/attendees/<int:attendee_id>', methods=['DELETE'])
def delete_attendee(event_id, attendee_id):
    service = DataService(get_db())
    service.remove_attendee(event_id, attendee_id)
    return jsonify({'status':'OK'}), 201


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
