#!/bin/bash
cd /my_work/flask_web/flask_studt/
source venv/bin/activate

export FLASK_APP=app.py
flask run --host=0.0.0.0 --debug
