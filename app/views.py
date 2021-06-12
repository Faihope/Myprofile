from flask import render_template
from app import app
from .forms import RegistrationForm,LoginForm

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - This is my profile'
    return render_template('index.html' ,title=title)

@app.route('/register')
def register():
    form = RegistrationForm()
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('register.html' ,form = form)


@app.route('/login')
def login():
    form = LoginForm()
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('login.html' ,form = form )