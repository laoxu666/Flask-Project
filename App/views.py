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


@blue.route("/addstudent/")
def add_student():

    student = Student()
    student.s_name = "小明%d" %random.randrange(100)

    db.session.add(student)
    db.session.commit()

    return "Student Create Success!"