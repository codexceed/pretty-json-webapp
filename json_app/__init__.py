"""Initializes the web app."""
from flask import Flask

app = Flask(__name__)

from json_app import routes  # NOQA
