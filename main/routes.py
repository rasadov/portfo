import os
from main import app, db
from flask import send_from_directory, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

class Message(FlaskForm):
    name = StringField(label='Name',validators=[DataRequired(),Length(min=2,max=40)])
    surname = StringField(label='Surname',validators=[Length(min=2,max=40)])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    message = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=50), nullable=True)
    email = db.Column(db.String(length=50), nullable=False)
    message = db.Column(db.String(),nullable=False)


class Articles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)

def thank_you():
    return render_template('thankyou.html')

@app.route('/', methods=['GET','POST'])
def my_home():
    form = Message()
    blog = Articles.query.all()
    if request.method == 'GET':
        return render_template('index.html', form=form, blog=blog, length=len(blog))
    
    if form.validate_on_submit():
        message = Contact(name=form.name.data,
                              surname = form.surname.data,
                              email = form.surname.data,
                              message = form.message.data)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('thankyou.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

