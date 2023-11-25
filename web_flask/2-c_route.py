#!/usr/bin/python3
""" Flask web application script """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Route for the root URL """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Route for the /hbnb URL """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Route for the /c/<text> URL """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
