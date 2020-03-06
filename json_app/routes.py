from flask import render_template, request

from json_app import app
from json_app.constants import HOME_TITLE


@app.route('/pretty-json')
def index() -> str:
    x = request.args
    return render_template('prettyjson.html', title=HOME_TITLE)
