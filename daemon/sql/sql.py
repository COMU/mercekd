#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import ConfigParser
import MySQLdb
from settings import ConfigClass
import os
#logging

class SqlManager:
    def __init__(self):
        connectionState=0
        conn=0

        config_class=ConfigClass()
        path=os.path.abspath("")
        config_class.config_file=open(path+"/"+"setting.config",'r')
        config_class.config.readfp(config_class.config_file)


        self.log_db=logging.getLogger("mercekd_db")
        self.log_db.setLevel(logging.ERROR)
        self.logger_db_console=logging.StreamHandler()
        formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.logger_db_console.setFormatter(formatter)
        self.log_db.addHandler(self.logger_db_console)

        try:
            self.server=config_class.config.get("Sql Settings","server")
            self.user_name=config_class.config.get("Sql Settings","user_name")
            self.passwd=config_class.config.get("Sql Settings","passwd")
            self.database_name=config_class.config.get("Sql Settings","database_name")
            config_class.config_file.close()

        except ConfigParser.NoOptionError:
            self.log_db.error("No option exist this section")

    def connect(self):
        try:
            self.conn=MySQLdb.connect(host=self.server,user=self.user_name,passwd=self.passwd,db=self.database_name)
            self.log_db.setLevel(logging.INFO)
            self.log_db.info("The connection is successful")
            self.logger_db_console.flush()
            self.connectionState=1
        except MySQLdb.DatabaseError:
            self.connectionState=0
            log_db.setLevel(logging.ERROR)
            log_db.error("Error: Database Connection")


    def insert(self, result):
        try:
            sql_query="INSERT INTO lease_db(`ip`,`mac`,`start`,`end`) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")" % ((result['ip'],result['ethernet'],result['start_time'],result['end_time']))
            result['uid']=None
            result['client-hostname']=None
            cursor=self.conn.cursor()
            cursor.execute(sql_query)
            self.conn.commit()
            self.log_db.setLevel(logging.INFO)
            self.log_db.info("A data is added in database")

        except MySQLdb.DataError:
            log_db.setLevel(logging.ERROR)
            log_db.error("Data does not exist")

    def close(self):
        self.conn.close()