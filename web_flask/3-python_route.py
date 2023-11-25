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


def display_c(text):
    """ Return a message for the /c/<text> route """
    return 'C {}'.format(text.replace('_', ' '))


def python_is_cool(text='is cool'):
    """ Return a message for the /python and /python/<text> routes """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/')
def hello_hbnb():
    """ Route for the root URL """
    return greet_hbnb()


@app.route('/hbnb')
def hbnb():
    """ Route for the /hbnb URL """
    return display_hbnb()


@app.route('/c/<text>')
def c_is_fun(text):
    """ Route for the /c/<text> URL """
    return display_c(text)


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ Route for the /python and /python/<text> URLs """
    return python_is_cool(text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
