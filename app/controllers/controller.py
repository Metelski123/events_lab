from flask import render_template, request, redirect
from app import app
# from app.models.event_list import event_list
from app.models.events import Event

@app.route('/')
def greet():
    return "Hello"