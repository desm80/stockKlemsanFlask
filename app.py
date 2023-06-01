from http import HTTPStatus

from flask import Flask, render_template

from forms import DownloadForm, PartNumberForm
from settings import Config
from utils import download_stocks, get_stock

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def klemsan_view():
    """
    Рендеринг формы и обработка запроса на проверку наличия на складах.
    """
    form = PartNumberForm()
    if form.validate_on_submit():
        part_number = form.part_number.data
        result = get_stock(part_number)
        # form.part_number = ''
        return render_template('klemsan.html', form=form, result=result)
    return render_template('klemsan.html', form=form)


@app.route('/download', methods=['GET', 'POST'])
def download_view():
    form = DownloadForm()
    if form.validate_on_submit():
        download_stocks()
        message = 'Остатки успешно загружены!'
        return render_template('download.html', form=form, message=message)
    return render_template('download.html', form=form)


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


if __name__ == '__main__':
    app.run()
