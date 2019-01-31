#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from apps import app,connect_db
from flask import jsonify

def hello_world():
    res=connect_db.execute_query("select *from admin")
    print res
    return jsonify(res)