from unicodedata import name
from mes_taches import app, login_manager, db
from flask import render_template, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from flask_login import login_user, logout_user, login_required, current_user

from mes_taches.models import Task, User
import datetime
from mes_taches.forms import AddTaskForm, LoginForm, RegisterForm, DeleteTaskForm, ChangeTaskStatusForm


@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    deleted_task_form = DeleteTaskForm()
    change_task_status_form = ChangeTaskStatusForm()

    if request.method == 'POST':
        deleted_task = request.form.get('deleted_task')
        change_task_status = request.form.get('change_task_status')
        if deleted_task:
            task = Task.query.get(deleted_task)
            db.session.delete(task)
            db.session.commit()
            flash(f'La tâche {task.title} a été supprimée', 'success')
        if change_task_status:
            task = Task.query.get(change_task_status)
            if task.status == 'Pas Commencé':
                task.status = 'En Cours'
            elif task.status == 'En Cours':
                task.status = 'Terminé'
            db.session.commit()
            flash(
                f'Le statut de la tâche {task.title} a été modifiée', 'success')
    tasks = Task.query.filter_by(author=current_user.id)
    return render_template('tasks.html', tasks=tasks, deleted_task_form=deleted_task_form, change_task_status_form=change_task_status_form)

# @app.route('/tasks/<int:task_id>')
# # @login_required
# def task(task_id):
#     # task = Task.query.get_or_404(task_id)
#     return render_template('task.html')


@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = AddTaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            task_to_create = Task(
                title=form.title.data,
                description=form.description.data,
                author=current_user.id,
                deadline=datetime.datetime.strptime(form.deadline.data, '%d/%m/%Y'),
                status="Pas Commencé"
            )
            db.session.add(task_to_create)
            db.session.commit()
            flash(f'La tâche {task_to_create.title} a été ajoutée', 'success')
            return redirect(url_for('tasks'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Il y a une erreur dans le formulaire: {err_msg}', 'danger')
    
    return render_template('add_task.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('Vous êtes déconnecté', category='info')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Vous êtes connecté', category='info')
            return redirect(url_for('tasks'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect', category='error')

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f'Compte créé avec succès! Vous êtes connecté en tant que {user_to_create.name}', category='success')
        return redirect(url_for('index'))

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f'Il y a une erreur dans le formulaire: {err_msg}', category='danger')

    return render_template('register.html', form=form)
