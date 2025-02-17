from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    DateField,
    SelectField,
    SelectMultipleField,  # Adicione esta importação
    SubmitField
)
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class SchoolForm(FlaskForm):
    name = StringField('Nome da Escola', validators=[DataRequired()])
    code = StringField('Código', validators=[DataRequired()])
    address = StringField('Endereço')
    submit = SubmitField('Salvar')


class ClassForm(FlaskForm):
    name = StringField('Nome da Turma', validators=[DataRequired()])
    year = StringField('Ano Letivo', validators=[DataRequired()])
    school = SelectField('Escola', coerce=int)
    submit = SubmitField('Salvar')


class TeacherForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    school = SelectField('Escola', coerce=int)
    submit = SubmitField('Salvar')


class StudentForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    birthdate = DateField('Data de Nascimento', format='%Y-%m-%d')
    schools = SelectMultipleField('Escolas', coerce=int)
    classes = SelectMultipleField('Turmas', coerce=int)
    submit = SubmitField('Salvar')
