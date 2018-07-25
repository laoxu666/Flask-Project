# 放各种扩展库
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 懒加载
def init_ext(app):

    db.init_app(app=app)

    return app