from flask import render_template, request, redirect, url_for

from json_app import app
from json_app.constants import HOME_TITLE
from json_app.parse_json import prettify


@app.route('/')
def index() -> str:
    """Pretty-json webpage endpoint."""
    x = request.args
    return redirect(url_for('prettify_json'))


@app.route('/prettify-json', methods=['POST', 'GET'])
def prettify_json() -> str:
    """Return prettified json text."""
    json_input = request.args.get('json-input')
    json_output = prettify(text=json_input)
    return render_template('prettyjson.html', title=HOME_TITLE, json_output=json_output)