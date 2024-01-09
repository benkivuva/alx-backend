#!/usr/bin/env python3
"""
Script that starts a basic Flask app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays info from 0-index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
