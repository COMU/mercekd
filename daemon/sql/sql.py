#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import ConfigParser
import MySQLdb
from settings import ConfigClass
import os
#logging
log_db=logging.getLogger("mercekd_db")
log_db.setLevel(logging.ERROR)
logger_db_console=logging.StreamHandler()
logger_db_console.setLevel(logging.ERROR)
formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_db_console.setFormatter(formatter)
log_db.addHandler(logger_db_console)
class SqlManager:
    def __init__(self):
        connectionState=0
        conn=0

        config_class=ConfigClass()
        path=os.path.abspath("")
        config_class.config_file=open(path+"/"+"setting.config",'r')
        config_class.config.readfp(config_class.config_file)

        try:
            self.server=config_class.config.get("Sql Settings","server")
            self.user_name=config_class.config.get("Sql Settings","user_name")
            self.passwd=config_class.config.get("Sql Settings","passwd")
            self.database_name=config_class.config.get("Sql Settings","database_name")

        except ConfigParser.NoOptionError:
            log_db.error("No option exist this section")

    def connect(self):
        try:
            self.conn=MySQLdb.connect(host=self.server,user=self.user_name,passwd=self.passwd,db=self.database_name)
            #log_db.setLevel(logging.INFO)
            log_db.info("The connection is successful")
            self.connectionState=1
        except MySQLdb.DatabaseError:
            self.connectionState=0
            log_db.setLevel(logging.ERROR)
            log_db.error("Error: Database Connection")


    def insert(self, result):

        try:
            sql_query=("""INSERT INTO lease_db(ip,mac,start,end) VALUES (%s,%s,%s,%s)""" ,(result['ip'],result['ethernet'],result['start_time'],result['end_time']))
            result['uid']=None
            result['client-hostname']=None
            cursor=self.conn.cursor()
            cursor.execute(sql_query)
            self.conn.commit()
            self.conn.close()
        except MySQLdb.DataError:
            log_db.setLevel(logging.ERROR)
            log_db.error("Data does not exist")