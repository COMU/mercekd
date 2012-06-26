#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import MySQLdb
class SqlManager:
    #readme.txt oluşturulmalı

    _connectionState=0
    _conn=0
    config=ConfigParser.RawConfigParser()
    config_file=open("settings.config",'r')
    config.readfp(config_file)

    def __init__(self):
        try:
            self.server=config.get("Sql Settings","server")
            self.user_name=config.get("Sql Settings","user_name")
            self.passwd=config.get("Sql Settings","passwd")
            self.database_name=config.get("Sql Settings","database_name")

        except ConfigParser.NoOptionError:
            print "No option exist in section"

    def connect(self):
        try:
            self._conn=MySQLdb.connect(host=self.server,user=self.user_name,passwd=self.passwd,db=self.database_name)
            self._connectionState=1
            print "bağlantı oluştu"
        except :
            self._connectionState=0
            print "bağlantı oluşmadı"
        return self._connectionState


    def insert(self, result):
        sql("""INSERT INTO lease_db(ip,mac,start,end,uid,client) VALUES (?,?,?,?,?,?)""" %(result['ip'],
        result['ethernet'],result['start_time'],result['end_time'],result['uid'],result['client-hostname']))

        cursor=self._conn.cursor()
        cursor.execute(sql)

        self._conn.commit()
        self._conn.close()