#!/usr/bin/python3
"""
Initiates a Flask web application.
Listens on 0.0.0.0 on port 5000.
Routes:
/hbnb_filters: HTML page for HBnB filters.
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
Shows the HTML page for HBnB filters."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the existing SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
