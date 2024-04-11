from typing import Optional as Opt
from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields.core import Field
from wtforms.fields.numeric import *
from wtforms.fields.simple import *
from wtforms.validators import InputRequired, Email, Optional, ValidationError

app = Flask(__name__)


def number_length(min: int = 0, max: int = 0, message: Opt[str] = None):

    if not message:
        message = 'Число должно быть неотрицательным, а длина должна находиться в указанном диапазоне.'

    def _number_length(form: FlaskForm, field: Field):
        if field.data is not None and len(str(field.data)) < min or len(str(field.data)) > max:
            raise ValidationError(message)

    return _number_length


class NumberLength:
    def __init__(self, min: int = 0, max: int = 0, message: Opt[str] = None):
        self.min = min
        self.max = max
        self.message = message or 'Число должно быть неотрицательным, а длина должна находиться в указанном диапазоне.'

    def __call__(self, form: FlaskForm, field: Field):
        if not self.message:
            self.message = 'Число должно быть неотрицательным, а длина должна находиться в указанном диапазоне.'

        if field.data is not None and len(str(field.data)) < self.min or len(str(field.data)) > self.max:
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(min=10, max=10)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[Optional()])


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f'Successfully registered user {email} with phone=7{phone} '

    return f'invalid input{form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True,port=5546)
