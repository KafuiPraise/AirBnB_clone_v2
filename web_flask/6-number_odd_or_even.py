#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Displays 'C' followed by the value of the text variable.

    Replaces underscores in the text with spaces.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Displays 'Python' followed by the value of the text variable.

    Replaces underscores in the text with spaces.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Displays '{} is number' only if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays an HTML page only if n is an integer.

    Uses Flask's render_template function to render the HTML page.
    Handles ValueError if n is not an integer.
    """
    try:
        return render_template('5-number.html', number=n)
    except ValueError:
        return 'Invalid input. Please provide an integer.'


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Shows if the number is even or odd.

    Displays an HTML page indicating whether the number is even or odd.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
