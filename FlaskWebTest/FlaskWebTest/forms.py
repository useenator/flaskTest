from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,PasswordField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email,Length, EqualTo
import models

def email_exists(form, field):
    if models.User.query.filter(models.User.email == field.data).first():
        raise ValidationError('User with that email already exists.')

def name_exists(form, field):
    check = models.User.query.filter(models.User.username == field.data).first()
    if check:
        raise ValidationError('User with that name already exists.')
        #raise ValidationError(self.message)

class LoginForm(Form):
    username = StringField('name', validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(Form):
    username = StringField('name',
            validators=[DataRequired(),
                        Regexp(r'^[a-zA-Z0-9_]+$',
                        message=("Username should be one word, letters, "
                         "numbers, and underscores only.")
                            ),
                            name_exists
                        ])

    email = StringField('email', validators=[
                                DataRequired(),
                                Email(),
                                email_exists
                        ])

    password=PasswordField('confirm password',validators=[
                    DataRequired(),
                    Length(min=2),
                    EqualTo('passwordc', message='Passwords must match')
                ])
    passwordc=PasswordField('passwordc',validators=[DataRequired()])

class UpdateUserForm(Form):
    username = StringField('name',
            validators=[DataRequired()])

    email = StringField('email',
            validators=[DataRequired()])

    password=PasswordField('confirm password',
            validators=[DataRequired(),
                    EqualTo('passwordc', message='Passwords must match')
                ])
    passwordc=PasswordField('passwordc',validators=[DataRequired()])
