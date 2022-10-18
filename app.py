from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eif2hkzn582bcei'
app.config['FLASK_APP'] = 'app.py'
app.config['FLASK_ENV'] = 'development'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

@app.route('/')
def index():
    return render_template('index.html')
    
