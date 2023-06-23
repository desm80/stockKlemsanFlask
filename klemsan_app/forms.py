from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PartNumberForm(FlaskForm):
    """
    Форма для шаблона Главной страницы.
    """
    part_number = StringField(
        'Введите артикул изделия',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(4, 10)]
    )
    submit = SubmitField('Проверить')


class DownloadForm(FlaskForm):
    """
    Форма для шаблона страницы загрузки складских остатков.
    """
    submit = SubmitField('Загрузить')
