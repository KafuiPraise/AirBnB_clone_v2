#!/usr/bin/python3
"""Initiates a Flask web application.
The application is set to listen on 0.0.0.0, port 5000.
Routes:
/states: Generates an HTML page featuring a list of all State objects.
/states/<id>: Creates an HTML page showcasing the specified state with <id>.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(exc):
    """ to close a database session"""
    storage.close()


@app.route('/cities_by_states')
def states_list():
    """ Route for the "/states_list". """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
