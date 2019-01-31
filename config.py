#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Configapp(object):

    IP_ALLOWED=["0.0.0.0","127.0.0.1","192.168.1.111","192.168.1.144","192.168.1.101"]
    # Run:
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5000

    DB_USERNAME = 'rferro'
    DB_PASSWORD = 'rferro2018**++'
    DB_HOST = '192.168.7.22'
    DB_PORT = '1987'
    DB_NAME = 'bitinka'
    DB_DRIVER = 'mysql+pymysql'

    # SQLAlchemy:
    SQLALCHEMY_DATABASE_URI = DB_DRIVER + '://'+ DB_USERNAME + ':' + DB_PASSWORD + '@'+ DB_HOST + ':' + DB_PORT + '/' + DB_NAME+"?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_RECYCLE = 1

class DevelopmentConfig(Configapp):
    DEVELOPMENT = True
    DEBUG = True
