from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app import app, db
from app.models import School, Class, Teacher, Student, User
from app.forms import (
    SchoolForm,
    ClassForm,
    TeacherForm,
    StudentForm,
    LoginForm
)

# ======================= Rotas Gerais =======================


@app.route('/')
def home():
    return redirect(url_for('auth.login'))

# ======================= Rotas de Admin =======================


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        abort(403)

    schools = School.query.count()
    teachers = Teacher.query.count()
    students = Student.query.count()

    return render_template('admin/dashboard.html',
                           schools=schools,
                           teachers=teachers,
                           students=students)

# ----------------------- Escolas -----------------------


@app.route('/admin/schools')
@login_required
def list_schools():
    if current_user.role != 'admin':
        abort(403)

    schools = School.query.all()
    return render_template('admin/schools.html', schools=schools)


@app.route('/admin/school/new', methods=['GET', 'POST'])
@login_required
def new_school():
    form = SchoolForm()

    if form.validate_on_submit():
        school = School(
            name=form.name.data,
            code=form.code.data,
            address=form.address.data
        )
        db.session.add(school)
        db.session.commit()
        flash('Escola cadastrada com sucesso!', 'success')
        return redirect(url_for('list_schools'))

    return render_template('admin/new_school.html', form=form)


@app.route('/admin/school/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_school(id):
    school = School.query.get_or_404(id)
    form = SchoolForm(obj=school)

    if form.validate_on_submit():
        form.populate_obj(school)
        db.session.commit()
        flash('Escola atualizada!', 'success')
        return redirect(url_for('list_schools'))

    return render_template('admin/edit_school.html', form=form, school=school)


@app.route('/admin/school/<int:id>/delete', methods=['POST'])
@login_required
def delete_school(id):
    school = School.query.get_or_404(id)
    db.session.delete(school)
    db.session.commit()
    flash('Escola excluída!', 'success')
    return redirect(url_for('list_schools'))

# ----------------------- Turmas -----------------------


@app.route('/admin/classes')
@login_required
def list_classes():
    classes = Class.query.all()
    return render_template('admin/classes.html', classes=classes)


@app.route('/admin/class/new', methods=['GET', 'POST'])
@login_required
def new_class():
    form = ClassForm()
    form.school.choices = [(s.id, s.name) for s in School.query.all()]

    if form.validate_on_submit():
        new_class = Class(
            name=form.name.data,
            year=form.year.data,
            school_id=form.school.data
        )
        db.session.add(new_class)
        db.session.commit()
        flash('Turma criada com sucesso!', 'success')
        return redirect(url_for('list_classes'))

    return render_template('admin/new_class.html', form=form)

# ----------------------- Professores -----------------------


@app.route('/admin/teachers')
@login_required
def list_teachers():
    teachers = Teacher.query.all()
    return render_template('admin/teachers.html', teachers=teachers)


@app.route('/admin/teacher/new', methods=['GET', 'POST'])
@login_required
def new_teacher():
    form = TeacherForm()
    form.school.choices = [(s.id, s.name) for s in School.query.all()]

    if form.validate_on_submit():
        teacher = Teacher(
            name=form.name.data,
            cpf=form.cpf.data,
            email=form.email.data,
            school_id=form.school.data
        )
        db.session.add(teacher)
        db.session.commit()

        # Criar usuário associado
        user = User(
            username=form.email.data,
            role='teacher',
            teacher_id=teacher.id
        )
        user.set_password('senha_inicial')
        db.session.add(user)
        db.session.commit()

        flash('Professor cadastrado!', 'success')
        return redirect(url_for('list_teachers'))

    return render_template('admin/new_teacher.html', form=form)

# ----------------------- Alunos -----------------------


@app.route('/admin/students')
@login_required
def list_students():
    students = Student.query.all()
    return render_template('admin/students.html', students=students)


@app.route('/admin/student/new', methods=['GET', 'POST'])
@login_required
def new_student():
    form = StudentForm()
    form.schools.choices = [(s.id, s.name) for s in School.query.all()]
    form.classes.choices = [(c.id, c.name) for c in Class.query.all()]

    if form.validate_on_submit():
        student = Student(
            name=form.name.data,
            cpf=form.cpf.data,
            email=form.email.data,
            birthdate=form.birthdate.data
        )

        # Adicionar escolas e turmas
        for school_id in form.schools.data:
            school = School.query.get(school_id)
            student.schools.append(school)

        for class_id in form.classes.data:
            cls = Class.query.get(class_id)
            student.classes.append(cls)

        db.session.add(student)
        db.session.commit()

        # Criar usuário
        user = User(
            username=form.email.data,
            role='student',
            student_id=student.id
        )
        user.set_password('senha_inicial')
        db.session.add(user)
        db.session.commit()

        flash('Aluno cadastrado!', 'success')
        return redirect(url_for('list_students'))

    return render_template('admin/new_student.html', form=form)

# ======================= Rotas de Professor =======================


@app.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    if current_user.role != 'teacher':
        abort(403)

    teacher = Teacher.query.get(current_user.teacher_id)
    classes = Class.query.filter_by(school_id=teacher.school_id).all()

    return render_template('teacher/dashboard.html',
                           teacher=teacher,
                           classes=classes)

# ======================= Rotas de Aluno =======================


@app.route('/student/dashboard')
@login_required
def student_dashboard():
    if current_user.role != 'student':
        abort(403)

    student = Student.query.get(current_user.student_id)
    return render_template('student/dashboard.html',
                           student=student)
