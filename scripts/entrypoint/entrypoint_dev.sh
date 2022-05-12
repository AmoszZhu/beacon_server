#!/usr/bin/env bash
uwsgi --http 0.0.0.0:59001 --socket 0.0.0.0:59003 --chdir /server -w manage:app --master --processes 2 --threads 2 --harakiri 180 --buffer-size 32768 --http-time 180