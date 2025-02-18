# app/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    classes = db.relationship('Class', backref='school', lazy=True)


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable=False)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120))
    school_id = db.Column(db.Integer, db.ForeignKey(
        'school.id'), nullable=False)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120))
    birthdate = db.Column(db.Date)
    schools = db.relationship(
        'School', secondary='student_school', backref='students')
    classes = db.relationship(
        'Class', secondary='student_class', backref='students')


student_school = db.Table('student_school',
                          db.Column('student_id', db.Integer, db.ForeignKey(
                              'student.id'), primary_key=True),
                          db.Column('school_id', db.Integer, db.ForeignKey(
                              'school.id'), primary_key=True)
                          )

student_class = db.Table('student_class',
                         db.Column('student_id', db.Integer, db.ForeignKey(
                             'student.id'), primary_key=True),
                         db.Column('class_id', db.Integer, db.ForeignKey(
                             'class.id'), primary_key=True)
                         )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, teacher, student
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
