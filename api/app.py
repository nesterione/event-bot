#!flenv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify 

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return "Hi, this is Events API <br> /api/v0.1/events - return all events"


events = [
  {
    'id':1,
    'title': 'Quiz',
    'description': 'Как обычно квиз',
    'date': '06.03.2017 19:00',
    'location': 'Red pub',
    'tags': ['bg']
  },
  {
    'id':2,
    'title': 'Лазертег',
    'description': 'Пиу-пиу. биби-биби.',
    'date': '~19.03.2017 10:00',
    'location': "",
    'tags': ['sport']
  }
]

@app.route('/api/v0.1/events', methods=['GET'])
def get_events():
    return jsonify(events)
     
if __name__ == '__main__':
    app.run(debug=True, port=6910)
