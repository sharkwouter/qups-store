from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class GegevensFormulier(FlaskForm):
    voornaam = StringField('Voornaam')
    achternaam = StringField('Achternaam', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    adres = StringField('Adres', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    plaats = StringField('Plaats', validators=[DataRequired()])
    submit = SubmitField('Bestel')
