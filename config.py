#!/usr/bin/env python
# coding=utf-8

import os

import settings

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flaskweb] '
    FLASK_MAIL_SENDER = 'Universe<1505586488@qq.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_POSTS_PER_PAGE = 20
    FLASK_FOLLOWERS_PER_PAGE = 20

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = settings.DB_URL

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = settings.DB_URL

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = settings.DB_URL

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }
