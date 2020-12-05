#!/bin/bash
cd server
source flask-venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=5555
