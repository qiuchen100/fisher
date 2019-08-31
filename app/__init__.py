"""
    created by 邱晨 on 2019/8/31 9:45 PM.
"""
from flask import Flask

__author__ = '邱晨'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

