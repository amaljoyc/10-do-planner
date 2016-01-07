from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class TodoForm(Form):
    todo_text = StringField('', validators=[Required()])
    submit = SubmitField('Add todo')
