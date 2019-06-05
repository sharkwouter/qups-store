from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class BestelFormulier(FlaskForm):
    aantal = IntegerField('Aantal', validators=[DataRequired()])
    submit = SubmitField('Bevestig aantal')
