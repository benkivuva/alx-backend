#!/usr/bin/env python3
"""
Script that starts a basic Flask app with Flask-Babel configuration
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class with available languages, default locale, and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index() -> str:
    """Function that displays info from 0-index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
