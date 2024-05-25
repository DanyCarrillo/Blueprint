#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import pymysql

class Connection():
    def __init__(self):
        host = ""
        user = "
        port = 1987
        password = ""
        db = ""
        self.con = pymysql.connect(host=host,port=port,user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def execute_query(self, query):
    	self.cur.execute(query)
        result = self.cur.fetchall()
        return result    