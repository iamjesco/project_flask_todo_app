from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
	
	title = StringField('Title', validators=[DataRequired('Please enter a proper title')])
	content = TextAreaField('Content', validators=[DataRequired('Please enter proper content')])