# 放各种扩展库
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()

# 懒加载
def init_ext(app):

    db.init_app(app=app)

    migrate.init_app(app=app, db=db)

    return app