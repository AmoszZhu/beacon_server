#! /bin/bash

source ~/.zshrc
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=manage
workon server
cd ..
flask run -h 0.0.0.0 -p 59003