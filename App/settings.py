# 配置
def get_db_uri(dbinfo):
    # 获取值，值若是不存在给个默认值
    BACKEND = dbinfo.get('BACKEND') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'rock1204'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or 3306
    DB = dbinfo.get('DB') or 'db'

    return "{}+{}://{}:{}@{}:{}/{}".format(BACKEND, DRIVER, USER, PASSWORD, HOST, PORT,DB)


class Config:

    SECRET_KEY = '123456789qwertyuiopadfghjklzxcvbnm'

    DEBUG = False

    TESTING = False

    # 为了将来程序升级预留扩展性
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 不同环境有不同配置
# 开发环境
class DevelopConfig(Config):

    DEBUG = True

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': 3306,
        'DB': 'PythonFlaskProject',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 测试环境
class TestingConfig(Config):

    TESTING = True

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'DB': 'PythonFlaskTesting',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 演示环境 和 线上环境一致
class StagingConfig(Config):

    DEBUG = False
    TESTING = False

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': 3306,
        'DB': 'PythonFlaskStaging',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 线上环境(生产环境)
class ProductConfig(Config):

    DATABASE = {
        'BACKEND': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': 3306,
        'DB': 'PythonFlaskProduct',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {

    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,

}