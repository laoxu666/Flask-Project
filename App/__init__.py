from flask import Flask

from App import settings
from App.ext import init_ext
from App.views import init_first_blue


def create_app():

    # app = Flask(__name__,template_folder='../templates')
    app = Flask(__name__)

    # 配置加载
    app.config.from_object(settings.envs.get("develop"))

    # 初始化各种第三方库
    init_ext(app)

    # 初始化蓝图
    init_first_blue(app)

    return app