from main.models import Admin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, Length


class Message(FlaskForm):
    name = StringField(label='Name',validators=[DataRequired(),Length(min=2,max=40)])
    surname = StringField(label='Surname',validators=[Length(min=2,max=40)])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    message = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class Article_Form(FlaskForm):
    title = StringField(label='Name',validators=[DataRequired()])
    text = StringField(label='Surname',validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class Project_Form(FlaskForm):
    title = StringField(label='Name',validators=[DataRequired()])
    text = StringField(label='Surname',validators=[DataRequired()])
    link = StringField(label='Surname',validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = Admin.query.filter_by(username=username_to_check.data).first()
        if user == None:
            raise ValidationError('Username already taken!')

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label=' Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
