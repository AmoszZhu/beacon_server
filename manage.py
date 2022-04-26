# -*- coding: utf-8 -*-

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"base dir : {BASE_DIR}")
sys.path.insert(0, os.path.join(BASE_DIR, 'common'))

from flask import jsonify

from apps import create_app
from common.settings.config import DevConfig

app = create_app(DevConfig, enable_config_file=True)

@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    :return:
    """
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})