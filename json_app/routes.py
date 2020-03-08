from flask import render_template, request

from json_app import app
from json_app.constants import HOME_TITLE
from json_app.parse_json import prettify


@app.route('/')
def index() -> str:
    """Pretty-json webpage endpoint."""
    x = request.args
    return render_template('prettyjson.html', title=HOME_TITLE)


@app.route('/prettify-json', methods=['POST', 'GET'])
def prettify_json() -> str:
    """Return prettified json text."""
    json_input = request.form.get('json-input')
    json_output = prettify(text=json_input)
    return render_template('prettyjson.html', title=HOME_TITLE, json_output=json_output)