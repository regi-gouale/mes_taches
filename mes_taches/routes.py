from mes_taches import app
from flask import render_template, request, redirect, url_for, flash, Blueprint
from jinja2 import TemplateNotFound
from flask_login import login_user, logout_user, login_required, current_user

# from mes_taches.models import Task
# from mes_taches import db

# from mes_taches.forms import TaskForm

@app.route('/')
@app.route('/index')
def index():
    # tasks = Task.query.all()
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    # form = TaskForm()
    # if form.validate_on_submit():
    #     task = Task(name=form.name.data, description=form.description.data)
    #     db.session.add(task)
    #     db.session.commit()
    #     flash('Task added successfully')
    #     return redirect(url_for('tasks'))
    # tasks = Task.query.all()
    return render_template('tasks.html')

# @app.route('/tasks/<int:task_id>')
# # @login_required
# def task(task_id):
#     # task = Task.query.get_or_404(task_id)
#     return render_template('task.html')

@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    # form = TaskForm()
    # if form.validate_on_submit():
    #     task = Task(name=form.name.data, description=form.description.data)
    #     db.session.add(task)
    #     db.session.commit()
    #     flash('Task added successfully')
    #     return redirect(url_for('tasks'))
    return render_template('add_task.html')

@app.route('/logout')
def logout():
    # logout_user()
    flash('Vous êtes déconnecté', category='info')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('index'))
    #     else:
    #         flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash(f'Your account has been created! You are now able to log in', 'success')
    #     return redirect(url_for('login'))
    return render_template('register.html')