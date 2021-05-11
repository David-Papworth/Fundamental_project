from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ArmyForm(FlaskForm):
    name = StringField('Name of the army', validators=[DataRequired()])
    description = StringField('Description of the Army')
    submit = SubmitField('Add Army')