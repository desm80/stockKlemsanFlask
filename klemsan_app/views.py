from flask import render_template

from klemsan_app import app, db
from klemsan_app.forms import PartNumberForm, DownloadForm
from klemsan_app.models import KlemsanStock
from klemsan_app.utils import download_stocks, xlsx_to_base


@app.route('/', methods=['GET', 'POST'])
def klemsan_view():
    """
    Рендеринг формы и обработка запроса на проверку наличия на складах.
    """
    form = PartNumberForm()
    if form.validate_on_submit():
        part_number = form.part_number.data
        result = KlemsanStock.query.filter(
            KlemsanStock.part_number.contains(part_number)).all()
        return render_template('klemsan.html', form=form, result=result)
    return render_template('klemsan.html', form=form)


@app.route('/download', methods=['GET', 'POST'])
def download_view():
    """
    Рендеринг формы с кнопкой для загрузки складских остатков и вывода
    сообщения, если загрузка прошла успешно.
    """
    form = DownloadForm()
    if form.validate_on_submit():
        # download_stocks.delay()
        download_stocks()
        db.drop_all()
        db.create_all()
        xlsx_to_base(['./downloads/eparh.xlsx',
                      './downloads/global.xlsx'])
        message = 'Остатки успешно загружены!'

        return render_template('download.html', form=form, message=message)
    return render_template('download.html', form=form)
