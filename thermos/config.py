import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # os.urandom(24)
    SECRET_KEY = '\x87\xd7\x14j\xee\x87\xbcS\x80\x98\xbc\x966q\xea\xd4\x03\x94s-\x96\x8d\x06\xbe'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)