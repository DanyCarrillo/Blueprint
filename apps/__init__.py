#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from flask import Flask
import os
from utils.connection import Connection

app = Flask(__name__)
app_settings = os.getenv('APP_SETTINGS','config.DevelopmentConfig')
app.config.from_object(app_settings)
connect_db = Connection()

from apps.login import login
app.register_blueprint(login)