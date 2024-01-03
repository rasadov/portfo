from main import app, db
import os
from flask import send_from_directory, render_template, request, redirect, url_for
from main.forms import Message, Project_Form, Article_Form, LoginForm
from main.models import Projects, Articles, Admin, Contact

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')




    

def add_to_database(model):
    db.session.add(model)
    db.session.commit()

def thank_you():
    return render_template('thankyou.html')

@app.route('/', methods=['GET','POST'])
def my_home():
    form = Message()
    projects = Projects.query.all()
    blog = Articles.query.all()
    if request.method == 'GET':
        return render_template('index.html', form=form, blog=blog[::-1], length=len(blog), projects=projects[::-1], plength=len(projects))
    
    if form.validate_on_submit():
        message = Contact(name=form.name.data,
                              surname = form.surname.data,
                              email = form.surname.data,
                              message = form.message.data)
        add_to_database(message)
        return redirect(url_for('thank_you'))
    return render_template('thankyou.html')


@app.route('/create-blog')
def create_blog():
    return render_template('create_blog.html')

def create_project():
    return render_template('create_project.html')

@app.route('/login')
def log_in():
    return render_template('login.html')


@app.route('/admin')
def admin():
    blog = Articles.query.all()
    projects = Projects.query.all()
    return render_template('admin.html', blog=blog[::-1], length=len(blog), projects=projects[::-1], plength=len(projects))
