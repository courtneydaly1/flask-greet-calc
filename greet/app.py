from flask import FLASK

app = FLASK(__name__)

@app.route('/welcome')
def index():
    return 'welcome'

@app.route('/welcome/home')
def home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'
