#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging


class SqlManager:

    def __init__(self):
        pass


    def insert(self, result):

        try:
            if not result.has_key('uid') and not result.has_key('client-hostname'):
                sql_query="INSERT INTO lease_db(`ip`,`mac`,`start`,`end`) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")" % ((result['ip'],result['ethernet'],result['start_time'],result['end_time']))
            if result.has_key('uid') and not result.has_key('client-hostname'):
                sql_query="INSERT INTO lease_db(`ip`,`mac`,`start`,`end`,`uid`) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % ((result['ip'],result['ethernet'],result['start_time'],result['end_time'],result['uid']))
            if result.has_key('client-hostname') and not result.has_key('uid'):
                sql_query="INSERT INTO lease_db(`ip`,`mac`,`start`,`end`,`client`) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",('\"%s\"'))" % ((result['ip'],result['ethernet'],result['start_time'],result['end_time'],(result['client-hostname'])))
            if result.has_key('uid') and result.has_key('client-hostname'):
                sql_query="INSERT INTO lease_db(`ip`,`mac`,`start`,`end`,`uid`,`client`) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",'\"%s\"')" % ((result['ip'],result['ethernet'],result['start_time'],result['end_time'],result['uid'],result['client-hostname']))

            cursor=self.conn.cursor()
            cursor.execute(sql_query)
            self.conn.commit()
            self.log_db.setLevel(logging.INFO)
            self.log_db.info("A data is added in database")
            result['uid']=None
            result['client-hostname']=None
        except MySQLdb.DataError:
            self.log_db.setLevel(logging.ERROR)
            self.log_db.error("Data does not exist")

    def close(self):
        self.conn.close()
