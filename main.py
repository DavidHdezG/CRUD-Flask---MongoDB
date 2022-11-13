import os

from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient
from classes import *

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
client = MongoClient("mongodb://localhost:27017/Scott")
db = client.Scott


def createDepto(form):
    depto = {
        'deptno': int(form.deptno.data),
        'dname': form.dname.data,
        'loc': form.loc.data
    }
    print(depto)
    print(db.dept.insert_one(depto))
    return redirect('/')


def deleteDepto(form):
    db.dept.delete_one({'deptno': int(form.deptno.data)})
    return redirect('/')


def updateDepto(form):
    depto = {
        'deptno': int(form.deptno.data),
        'dname': form.dname.data,
        'loc': form.loc.data
    }
    db.dept.update_one({'deptno': int(form.deptno.data)}, {'$set': depto})
    return redirect('/')


def createEmp(form):
    emp = {
        'empno': int(form.empno.data),
        'ename': form.ename.data,
        'job': form.job.data,
        'mgr': int(form.mgr.data),
        'hiredate': form.hiredate.data,
        'sal': int(form.sal.data),
        'comm': int(form.comm.data),
        'deptno': int(form.deptno.data)
    }
    db.emp.insert_one(emp)
    return redirect('/')


def updateEmp(form):
    emp = {
        'empno': int(form.empno.data),
        'ename': form.ename.data,
        'job': form.job.data,
        'mgr': int(form.mgr.data),
        'hiredate': form.hiredate.data,
        'sal': int(form.sal.data),
        'comm': int(form.comm.data),
        'deptno': int(form.deptno.data)
    }
    db.emp.update_one({'empno': int(form.empno.data)}, {'$set': emp})
    return redirect('/')


def deleteEmp(form):
    db.emp.delete_one({'empno': int(form.empno.data)})
    return redirect('/')


def readAllEmp():
    data = []
    for i in db.emp.find({}, {"_id": 0}):
        data.append(i)
    return data


def readAllDept():
    data = []
    for i in db.dept.find({}, {"_id": 0}):
        data.append(i)
    return data


@app.route('/', methods=['GET', 'POST'])
def main():
    cformDept = CreateDept(prefix='cformDept')
    dformDept = DeleteDept(prefix='dformDept')
    uformDept = UpdateDept(prefix='uformDept')
    cformEmp = CreateEmp(prefix='cformEmp')
    dformEmp = DeleteEmp(prefix='dformEmp')
    uformEmp = UpdateEmp(prefix='uformEmp')

    if cformDept.validate_on_submit():
        return createDepto(cformDept)
    if dformDept.validate_on_submit():
        return deleteDepto(dformDept)
    if uformDept.validate_on_submit():
        return updateDepto(uformDept)
    if cformEmp.validate_on_submit():
        return createEmp(cformEmp)
    if dformEmp.validate_on_submit():
        return deleteEmp(dformEmp)
    if uformEmp.validate_on_submit():
        return updateEmp(uformEmp)

    return render_template('index.html', cformDept=cformDept, dformDept=dformDept, uformDept=uformDept,
                           cformEmp=cformEmp, dformEmp=dformEmp, uformEmp=uformEmp, dataEmp=readAllEmp(),
                           dataDept=readAllDept())


if __name__ == "__main__":
    app.run(debug=True)
