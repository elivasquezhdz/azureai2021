from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired,Length
class TextForm(FlaskForm):
    text = TextAreaField()
    submit = SubmitField('Submit')