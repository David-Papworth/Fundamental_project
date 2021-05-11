from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class ArmyForm(FlaskForm):
    name = StringField('Name of the army', validators=[DataRequired()])
    description = StringField('Description of the Army')
    submit = SubmitField('Add Army')

class FigureForm(FlaskForm):
    name = StringField('Name of the figure', validators=[DataRequired()])
    number_of_models = IntegerField('number of models', validators=[DataRequired()])
    faction = SelectField('The faction the figure is from', choices=[], validators=[DataRequired()])
    army = SelectField('Which army is this figure in', choices=[])
    submit = SubmitField('Add Figures')
