from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange


class CreateDept(FlaskForm):
    deptno = IntegerField('Número de departamento', validators=[InputRequired()])
    dname = TextField('Nombre del departamento', validators=[InputRequired()])
    loc = TextField('Localización', validators=[InputRequired()])
    create = SubmitField('Agregar')


class DeleteDept(FlaskForm):
    deptno = TextField('Número de departamento', validators=[InputRequired() , Length(min=2, max=2)])
    delete = SubmitField('Eliminar')


class UpdateDept(FlaskForm):
    deptno = IntegerField('Número de departamento', validators=[InputRequired(), Length(min=2, max=2)])
    dname = TextField('Nombre del departamento', validators=[InputRequired()])
    loc = TextField('Localización', validators=[InputRequired()])
    update = SubmitField('Actualizar')

class CreateEmp(FlaskForm):
    empno = IntegerField('Número de empleado', validators=[InputRequired(), Length(min=0, max=4)])
    ename = TextField('Nombre del empleado', validators=[InputRequired()])
    job = TextField('Trabajo', validators=[InputRequired()])
    mgr = IntegerField('Número de jefe', validators=[InputRequired(), Length(min=0, max=4)])
    hiredate = TextField('Fecha de contratación', validators=[InputRequired()])
    sal = IntegerField('Salario', validators=[InputRequired(), Length(min=2, max=7)])
    comm = IntegerField('Comisión', validators=[InputRequired(), Length(min=2, max=7)])
    deptno = IntegerField('Número de departamento', validators=[InputRequired(), Length(min=2, max=2)])
    create = SubmitField('Agregar')

class DeleteEmp(FlaskForm):
    empno = IntegerField('Número de empleado', validators=[InputRequired(), Length(min=0, max=4)])
    delete = SubmitField('Eliminar')

class UpdateEmp(FlaskForm):
    empno = IntegerField('Número de empleado', validators=[InputRequired(), Length(min=0, max=4)])
    ename = TextField('Nombre del empleado', validators=[InputRequired()])
    job = TextField('Trabajo', validators=[InputRequired()])
    mgr = IntegerField('Número de jefe', validators=[InputRequired(), Length(min=0, max=4)])
    hiredate = TextField('Fecha de contratación', validators=[InputRequired()])
    sal = IntegerField('Salario', validators=[InputRequired(), Length(min=2, max=7)])
    comm = IntegerField('Comisión', validators=[InputRequired(), Length(min=2, max=7)])
    deptno = IntegerField('Número de departamento', validators=[InputRequired(), Length(min=2, max=2)])
    update = SubmitField('Actualizar')

