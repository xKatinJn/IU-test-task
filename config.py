import os


class Config(object):
    SECRET_KEY = os.urandom(128)

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{os.getenv("DB_PASSWORD")}@localhost/iu_test_task_db' \
                              or 'database_uri'
