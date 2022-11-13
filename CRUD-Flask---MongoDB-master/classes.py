from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange


class CreateDept(FlaskForm):
    deptno = IntegerField('Número de departamento', validators=[InputRequired()])
    dname = TextField('Nombre del departamento', validators=[InputRequired()])
    loc = TextField('Localización', validators=[InputRequired()])
    create = SubmitField('Insert')


class DeleteDept(FlaskForm):
    deptno = TextField('Número de departamento', validators=[InputRequired()])
    delete = SubmitField('Delete')


class UpdateDept(FlaskForm):
    deptno = IntegerField('Número de departamento', validators=[InputRequired()])
    dname = TextField('Nombre del departamento', validators=[InputRequired()])
    loc = TextField('Localización', validators=[InputRequired()])
    update = SubmitField('Update')

class CreateEmp(FlaskForm):
    empno = IntegerField('Número de empleado', validators=[InputRequired()])
    ename = TextField('Nombre del empleado', validators=[InputRequired()])
    job = TextField('Trabajo', validators=[InputRequired()])
    mgr = IntegerField('Número de jefe', validators=[InputRequired()])
    hiredate = TextField('Fecha de contratación', validators=[InputRequired()])
    sal = IntegerField('Salario', validators=[InputRequired()])
    comm = IntegerField('Comisión', validators=[InputRequired()])
    deptno = IntegerField('Número de departamento', validators=[InputRequired()])
    create = SubmitField('Insert')

class DeleteEmp(FlaskForm):
    empno = IntegerField('Número de empleado', validators=[InputRequired()])
    delete = SubmitField('Delete')

class UpdateEmp(FlaskForm):
    empno = IntegerField('Número de empleado', validators=[InputRequired()])
    ename = TextField('Nombre del empleado', validators=[InputRequired()])
    job = TextField('Trabajo', validators=[InputRequired()])
    mgr = IntegerField('Número de jefe', validators=[InputRequired()])
    hiredate = TextField('Fecha de contratación', validators=[InputRequired()])
    sal = IntegerField('Salario', validators=[InputRequired()])
    comm = IntegerField('Comisión', validators=[InputRequired()])
    deptno = IntegerField('Número de departamento', validators=[InputRequired()])
    update = SubmitField('Update')

