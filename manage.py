# -*- coding: utf-8 -*-

from flask import jsonify

from apps import create_app
from common.settings.config import DevConfig

app = create_app(DevConfig, enable_config_file=True)

@app.route('/index')
def hello_world():
    app.logger.error("hello world")
    return 'Hello World'


@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    :return:
    """
    app.logger.info("start app")
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})