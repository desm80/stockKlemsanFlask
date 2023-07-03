from http import HTTPStatus

from flask import render_template

from klemsan_app import app


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """
    Кастомный обработчик ошибки 404.
    """
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """
    Кастомный обработчик ошибки 500.
    """
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
