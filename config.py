import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-know'
    TOKEN_TIME_EXPIRE = 3
    ALGORITHMS_TYPE = "HS256"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CUSTOMER_FORECAST_FOLDER = os.path.join(basedir, 'upload/forecast/')
    USER_LIST_FOLDER = os.path.join(basedir, 'upload/account/')
    EXPORT_OP_FOLDER = os.path.join(basedir, 'download/export_op/')
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024  # Default 4MB

    LOG_FORMAT = '%(asctime)s %(levelname)s:%(message)s'
    LOG_FILE_SIZE = 5 * 1024 * 1024
    LOG_NUM_BACKUP = 5

    # app context
    PERMISSION = None

    USER_ID = None
    ARR_USER_ID = None
    TEAM_ID = None
