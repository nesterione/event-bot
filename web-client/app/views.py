# coding: utf-8
from flask import render_template, redirect, url_for, request
from app import app
import requests
import json


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    host = app.config['BASE_URL']

    r = requests.get(url=host + '/api/v0.1/events')

    return render_template("index.html",
                           title='Home',
                           events=r.json())


@app.route('/event/<string:event_id>', methods=['GET'])
def get_event(event_id):
    host = app.config['BASE_URL']

    r = requests.get(url=host + '/api/v0.1/events/' + event_id)
    event = r.json()

    event['count'] = len(event['attendees'])

    return render_template("event.html",
                           title='Event',
                           event=event)


@app.route('/event/<string:event_id>/attendees', methods=['POST'])
def add_attendee(event_id):
    host = app.config['BASE_URL']

    name = request.form.get('name')
    notes = request.form.get('notes')
    # headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", 'data': data}
    data = {'name': name, "notes": notes}
    url = host + '/api/v0.1/events/' + event_id + '/attendees'
    headers = {'Content-Type': 'application/json'}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    print(r)
    return redirect(url_for('get_event', event_id=event_id))
