#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from . import login
from apps.login.controller import *

login.add_url_rule('/hola',view_func = hello_world,methods=['GET'])
