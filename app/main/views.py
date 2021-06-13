from flask import render_template,flash,redirect,url_for
from . import main
from .forms import RegistrationForm,LoginForm
from flask_login import login_required

# Views
@main.route('/')
@main.route("/home")
def home():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - This is my profile'
    return render_template('index.html' ,title=title)

@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')


@main.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
        
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Register'
    return render_template('register.html' ,title=title,form = form)


@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Login'
    return render_template('login.html' ,title=title,form = form )