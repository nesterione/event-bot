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


@app.route('/event/new', methods=['GET'])
def new_event():
    return render_template("edit_event.html", title='New Event')


@app.route('/event/new', methods=['POST'])
def save_new_event():
    r = process_event(request)
    return redirect(url_for('index'))


def process_event(req, id=None):
    title = req.form.get('title')
    description = req.form.get('description')
    location = req.form.get('location')
    date = req.form.get('date')
    price = req.form.get('price')
    tags = list(set([tag.strip() for tag in req.form.get('tags').split(' ')]))

    data = {'title': title,
            'description': description,
            'location': location,
            'date': date,
            'price': price,
            'tags': tags}

    if id != None:
        data['_id'] = id

    host = app.config['BASE_URL']
    url = host + '/api/v0.1/events'
    headers = {'Content-Type': 'application/json'}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r


@app.route('/event/<string:event_id>/edit', methods=['GET'])
def open_edit_event(event_id):
    host = app.config['BASE_URL']

    r = requests.get(url=host + '/api/v0.1/events/' + event_id)
    event = r.json()
    event['tags'] = " ".join(event['tags'])
    return render_template("edit_event.html",
                           title='Edit Event',
                           event=event)


@app.route('/event/<string:event_id>/edit', methods=['POST'])
def save_edit_event(event_id):
    r = process_event(request,event_id)
    return redirect(url_for('get_event', event_id=event_id))


@app.route('/event/<string:event_id>/delete', methods=['POST'])
def delete_event(event_id):
    host = app.config['BASE_URL']
    requests.delete(url=host + '/api/v0.1/events/' + event_id)
    return "", 200


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
    # print(r)
    return redirect(url_for('get_event', event_id=event_id))
