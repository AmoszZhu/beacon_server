# -*- coding: utf-8 -*-

from flask import jsonify
from flask_migrate import Migrate

from apps import create_app
from common.settings.config import DevConfig

app = create_app(DevConfig, enable_config_file=True)

from common.models import db
migrate = Migrate(app, db)


@app.route('/index')
def hello_world():
    return "Hello World"


@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    :return:
    """
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})