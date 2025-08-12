import random

from flask import Response
from flask_login import login_user, logout_user, current_user, login_required

from models import User
from flask_playground import app , render_template ,request , flash , redirect , url_for , db
import pytz, datetime
from forms import RegistrationForm , LoginForm
from flask_playground import bcrypt
from web_playground import post_pydantic
feedback = []




def store_feedback(url):
    feedback.append(dict(url=url, user=current_user.username, date=datetime.datetime.now(pytz.UTC)))
    # print(feedback)
    app.logger.info('stored feedback :' + url)

def num_feedback(num):
    return sorted(feedback,key= lambda bm:bm['date'],reverse=True)[:num]

@app.route('/')
@app.route('/root')  # can add multiple routes
def root():
    return render_template('index.html',new_feedback=num_feedback(3))  # render using jinja templates. index.html dervices from base


@app.route('/home')
def home():
    return """
    added a new sub-domain implementation
    """


@app.route('/add', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        url = request.form['feedback']
        store_feedback(url)
        flash("your feedback:" + url)
        return redirect(url_for('root'))  # redirect to home page
    return render_template('feedback.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def create_user(username, email, password):
    pwd_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password=pwd_hash)
    db.session.add(user)
    db.session.commit()


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('root'))
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('account created')
        create_user(request.form['username'], request.form['email'], request.form['password'])
        # print(User.query.all()) # retrieves the users from the table
        return redirect(url_for('login'))
    if form.errors:
        flash('validation errors:' + str(form.errors))
        app.logger.info('validation error:' + str(form.errors))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_rec = validate_login(request.form['email'],request.form['password'])
        if user_rec is not None:
            login_user(user_rec)
            return redirect(url_for('root'))
        else:
            flash('login failed')
    return render_template('login.html', title='login', form=form)

def validate_login(email,password):
    user_rec = User.query.filter_by(email=email).first()
    print(type(user_rec))
    if bcrypt.check_password_hash(user_rec.password,password):
        return user_rec
    else:
        return None

@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/posts',methods=['GET'])
@login_required
def posts():
    post_entry = post_pydantic.post_pyd(userID=current_user.id,id=random.randint(1,100),title='temporary post',
                                        body='this post is temporary and will be deleted soon')
    return Response(post_entry.model_dump_json(),mimetype='application/json')