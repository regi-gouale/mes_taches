from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from mes_taches.models import User


class RegisterForm(FlaskForm):
    name = StringField(label="Votre nom", validators=[
                       Length(min=2, max=32), DataRequired()])
    username = StringField(label="Votre pseudo", validators=[
                           Length(min=2, max=32), DataRequired()])
    email = StringField(label="Votre email", validators=[
                        Email(), DataRequired()])
    password = PasswordField(label="Votre mot de passe", validators=[
                             Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label="Confirmez votre mot de passe", validators=[
                                          DataRequired(), EqualTo('password')])
    submit = SubmitField(label="S'inscrire")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Ce pseudo est déjà pris. Veuillez en choisir un autre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'Cet email est déjà pris. Veuillez en choisir un autre.')


class LoginForm(FlaskForm):
    username = StringField(label="Votre pseudo", validators=[DataRequired()])
    password = PasswordField(label="Votre mot de passe",
                             validators=[DataRequired()])
    remember_me = BooleanField(label="Se souvenir de moi")
    submit = SubmitField(label="Se connecter")


class AddTaskForm(FlaskForm):
    title = StringField(label="Titre de la tâche", validators=[DataRequired()])
    description = StringField(label="Description", validators=[DataRequired()])
    deadline = StringField(label="Date limite", validators=[DataRequired()])
    status = StringField(label="Statut", validators=[
                         DataRequired()], default="Pas Commencé")
    author = StringField(label="Auteur", validators=[DataRequired()], default="admin")
    submit = SubmitField(label="Ajouter")


class DeleteTaskForm(FlaskForm):
    submit = SubmitField(label="Supprimer")


class ChangeTaskStatusForm(FlaskForm):
    submit = SubmitField(label="Changer le statut")
