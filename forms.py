'''
    forms.py for the learn new things app
'''

#  https://flask-wtf.readthedocs.io/en/stable/


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextField, PasswordField, validators, RadioField
from wtforms.validators import DataRequired, NumberRange, EqualTo, Email, Regexp, Length, ValidationError, InputRequired
from datamodels import db, thingstolearn, users


class MyForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])


class SignupForm(FlaskForm):
    fname       = StringField("First name", validators=[Length(min=1)])
    lname       = StringField("Last name", validators=[Length(min=1)])
    username    = StringField("Username", validators=[Regexp("\A[a-zA-Z0-9]+\Z")])
    email       = StringField("Email Address", validators=[Email()])
    #yes_TOS     = BooleanField('I accept the Terms of Service', validators=[InputRequired()])
    password    = PasswordField("Passphrase (min 12 char)", validators=[Length(min=12, message='Password must be at least 12 characters long.'),
                EqualTo("passrepeat", message="Passwords must match.")
    ])
    passrepeat  = PasswordField("Re-type passphrase")
    group       = StringField("What do you want to learn first? (optional)")

    '''
    def username_is_valid(self, field): # TODO change error type???
        if User.exists(query = {"username": field.data}):
            raise RuntimeError("That username is already in use.")

    def validate_email(self, field): 
        if User.exists(query = {"email": field.data}):
            raise ValidationError("That email address is already in use.")
    '''


# this class will handle returning user login
class LoginForm(FlaskForm):
    uname       = StringField("Username", validators=[DataRequired()])
    passphrase  = PasswordField("Passphrase", validators=[DataRequired()])

    def __init__(self, *a, **kw):
        self.validated_user = None
        super(LoginForm, self).__init__(*a, **kw)

    def validate_username_or_email(self, field):
        '''
            ingests username+password data
            and determines whether those are a match with 
            an existing user in the users collection.
        '''
        try:
            if (db.users.find({"username":field.data}).count() > 0):
                someuser = db.users.find_one({"username":field.data})
                the_hash = someuser["password_hash"] # the right answer
                if pbkdf2_sha512.verify(field.data, the_hash):
                    self.validated_user = validate(field.data, self.passphrase.data)
        except RuntimeError:
            raise ValidationError("Invalid username/email or password.")


    # TODO check understanding: this was (self, field) ... okay to change?
    # http://wtforms.readthedocs.io/en/latest/validators.html#custom-validators
    # def validate_username_or_email(self, field):

class WordForm(FlaskForm):
    word_guess = StringField("Type the word:", validators=[DataRequired()])




