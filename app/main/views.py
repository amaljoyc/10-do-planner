from flask import render_template, redirect, url_for, flash, request, json
from .. import db
from ..models import Todo
from . import main
from .forms import TodoForm


@main.route('/', methods=['GET', 'POST'])
def todo_form():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(text=form.todo_text.data)
        db.session.add(todo)
        db.session.commit()
        flash('New todo added!!')
        return redirect(url_for('.todo_form'))
    todos = Todo.query.all()
    return render_template(
        'todo-form.html', form=form, todos=todos)


@main.route('/edit_todo', methods=['GET', 'POST'])
def edit_todo():
    id = request.form["pk"]
    todo = Todo.query.get(id)
    todo.text = request.form["value"]
    db.session.commit()
    return json.dumps({})
