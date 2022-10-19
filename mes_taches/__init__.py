
from flask import Flask
import os


base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '../templates')

app = Flask(__name__, template_folder=template_dir)

app.config['SECRET_KEY'] = 'ef67c8c0-8b1e-4c1e-9c1e-8b1e4c1e9c1e'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['FLASK_APP'] = 'app.py'
app.config['FLASK_ENV'] = 'development'
# app.config['DEBUG'] = True

