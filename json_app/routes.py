"""Defines API endpoints."""
from typing import Any

from flask import redirect, render_template, url_for
from flask_request_validator import FORM, Param, validate_params
from werkzeug import Response

from json_app import app
from json_app.constants import HOME_TITLE
from json_app.parse_json.parser import prettify


@app.route("/")
def index() -> Response:
    """Pretty-json webpage endpoint."""
    return redirect(url_for("get_pretty_json"))


@app.route("/prettify-json", methods=["GET"])
def get_pretty_json() -> Any:
    """Return the prettyjson webpage."""
    return render_template("prettyjson.html", title=HOME_TITLE)


@app.route("/prettify-json", methods=["POST"])
@validate_params(Param("json-input", FORM, str))
def prettify_json(json_input: str) -> Any:
    """Return prettified json text."""
    try:
        json_output = prettify(text=json_input)
    except Exception:
        return "Invalid json string.", 400

    return render_template("prettyjson.html", title=HOME_TITLE, json_output=json_output)
