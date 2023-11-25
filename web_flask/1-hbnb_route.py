#!/usr/bin/python3
""" Flask web application script """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


def greet_hbnb():
    """ Return a greeting message """
    return 'Hello HBNB!'


def display_hbnb():
    """ Return a message for the /hbnb route """
    return 'HBNB'


@app.route('/')
def hello_hbnb():
    """ Route for the root URL """
    return greet_hbnb()


@app.route('/hbnb')
def hbnb():
    """ Route for the /hbnb URL """
    return display_hbnb()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
