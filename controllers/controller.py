from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_event_to_list, remove_event_from_list
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_guests = request.form['guests']
    event_location = request.form['location']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring)
    add_event_to_list(new_event)
    return redirect('/events')

@app.route('/events/delete/<int:event_num>', methods=['POST'])
def remove_event(event_num):
    event_to_delete = events[event_num - 1] 
    remove_event_from_list(event_to_delete)
    return redirect('/events')