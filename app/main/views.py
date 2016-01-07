from flask import render_template, session, redirect, url_for, flash
from .. import db
from ..models import Todo
from . import main
from .forms import TodoForm


@main.route('/', methods=['GET', 'POST'])
def todo_form():
    form = TodoForm()
    if form.validate_on_submit():
        session['todo_text'] = form.todo_text.data
        todo = Todo(text=session.get('todo_text'))
        db.session.add(todo)
        db.session.commit()
        flash('New todo added!!')
        return redirect(url_for('.todo_form'))
    return render_template(
        'todo-form.html', form=form, todo_text=session.get('todo_text'))
