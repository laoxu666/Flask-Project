import random

from flask import Blueprint

from App.ext import db

from App.models import Student

blue = Blueprint("first_blue",__name__)

# 懒加载
def init_first_blue(app):

    app.register_blueprint(blueprint=blue)


@blue.route("/")
def index():
    return "Hello Flask Project！"


# 添加数据
@blue.route("/addstudent/")
def add_student():

    student = Student()
    student.s_name = "小明%d" % random.randrange(100)
    # 添加数据操作
    db.session.add(student)
    db.session.commit()

    return "Student Create Success!"


# 添加一组数据
@blue.route("/addstudents/")
def add_students():

    students = []

    for i in range(10):

        student = Student()
        student.s_name = "小王%d" % random.randrange(100)

        students.append(student)

    # 添加一组学生
    db.session.add_all(students)
    db.session.commit()

    return "一组学生创建成功！"


# 先查询后删除
@blue.route("/deletestudent/")
def delete_student():

    student = Student.query.first()
    # 删除数据操作
    db.session.delete(student)
    db.session.commit()

    return "Student Delete Success!"


# 先查询后修改
@blue.route("/modifystudent/")
def modify_student():
    student = Student.query.first()
    student.s_name = "小花3"

    db.session.add(student)
    db.session.commit()

    return "修改学生成功！"
