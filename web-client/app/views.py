# coding: utf-8
from flask import render_template
from app import app
import requests


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    host = app.config['BASE_URL']

    r = requests.get(url= host + '/api/v0.1/events')

    return render_template("index.html",
                           title='Home',
                           events=r.json())
