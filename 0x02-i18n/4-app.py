#!/usr/bin/env python3
"""
Script that starts a basic Flask app with Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """
    Render the index template with the determined locale or the default locale

    Returns:
        str: Rendered HTML content.
    """
    return render_template('4-index.html', locale=get_locale()
                           or babel.default_locale)


class Config(object):
    """
    Configuration class for Flask app with Babel support.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """
    Determine the best-matched language based on the request's 'locale'
    parameter or the accepted languages in the request headers.

    Returns:
        str: Best-matched language code.
    """
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(debug=True)
