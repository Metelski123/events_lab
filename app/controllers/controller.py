from flask import render_template, request, redirect
from app import app
from app.models.event_list import events
from app.models.events import Event

@app.route('/')
def greet():
    return "Hello"

@app.route('/events')
def event_listings_long():
    return render_template('long.html', title='Events', events=events)

@app.route('/events', methods=['POST'])
def create_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_guests = request.form['guests']
    event_room = request.form['room']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_room, event_description)
    events.append(new_event)
    return redirect('/events')


@app.route('/events/short')
def event_listings_short():
    return render_template('short.html', title='Events', events=events)


    