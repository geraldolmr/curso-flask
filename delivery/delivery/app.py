from flask import Flask

from delivery.ext import site
from delivery.ext import config
from delivery.ext import toolbar
from delivery.ext import db
from delivery.ext import cli
from delivery.ext import migrate
from delivery.ext import hooks
from delivery.ext import admin
from delivery.ext import auth
from delivery.ext import babel


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    return app
