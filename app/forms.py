from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters long."),
            Regexp(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9\W])(?!.*\s).+$",
                message="Password must include uppercase, lowercase, a number or special symbol, and no spaces.",
            ),
        ],
    )
    submit = SubmitField("Create account")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")
