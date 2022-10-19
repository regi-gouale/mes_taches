from mes_taches import app, template_dir, db
from mes_taches import routes

app.add_url_rule('/', view_func=routes.index)
app.add_url_rule('/index', view_func=routes.index)
app.add_url_rule('/about', view_func=routes.about)
app.add_url_rule('/tasks', view_func=routes.tasks, methods=['GET', 'POST'])
app.add_url_rule('/add_task', view_func=routes.add_task, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=routes.logout)
app.add_url_rule('/login', view_func=routes.login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=routes.register)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, use_reloader=True)
