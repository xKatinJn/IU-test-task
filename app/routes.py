from app import app, db

from flask import render_template


@app.route('/', methods=['GET'])
def index():
    return '200'
