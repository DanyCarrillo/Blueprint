#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from flask import Blueprint
login = Blueprint('login',__name__)
from . import routes