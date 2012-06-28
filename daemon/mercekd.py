#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tailer
import sys
import logging
from optparse import OptionParser
from sql.sql import SqlManager
from datetime import datetime

#tail
if __name__ == "__main__":
    #logging
    log=logging.getLogger("mercekd")
    log.setLevel(logging.DEBUG)
    logger_console=logging.StreamHandler()
    formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_console.setFormatter(formatter)
    log.addHandler(logger_console)

    #options
    program='mercekd'
    parser = OptionParser(usage='usage: %prog [options] filepath')
    parser.add_option("-p", "--path",dest="path",help="the path of DHCP lease file",metavar="path")
    parser.add_option("-v","--verbose",dest="verbose",action='store_true',default=False)
    (option,args)=parser.parse_args()


    file_name=None
    if option.path:
        file_name=option.path
    if option.verbose:
        verbose=True
    if not option.verbose and not option.path:
        parser.print_help()
        sys.exit(1)


    log.info("mercekd started")
    sql = SqlManager()
    sql.connect()
    try:
      if file_name:
        result=dict()
        flag = False
        for line in tailer.follow(open(file_name)):
            if line.startswith('lease'):
                flag = True
                lease=line.split()
                ip=lease[1]
                result['ip']=ip
                continue

            if line.strip().startswith("}"):
                log.info("IP=%s MAC=%s" % (result['ip'], result['ethernet']))
                logger_console.flush()
                flag = False
                sql.insert(result)

            if flag:
                if line.strip().startswith('starts'):
                    li = line.strip().split()
                    start_time=" ".join(li[2:])
                    result['start_time']=start_time
                    if option.verbose:
                        log.debug("Start time: %s" % (start_time))

                    time_format="%Y/%m/%d %H:%M:%S;"
                    result['start_time']=datetime.strptime(start_time,time_format)
                    continue

                if line.strip().startswith('ends'):
                    li = line.strip().split()
                    end_time=" ".join(li[2:])
                    result['end_time']=end_time
                    if option.verbose:
                        log.debug("End time: %s" % (end_time))

                    time_format="%Y/%m/%d %H:%M:%S;"
                    result['end_time']=datetime.strptime(end_time,time_format)
                    continue

                if line.strip().startswith('hardware'):
                    li = line.strip().split()
                    ethernet=li[2]
                    result['ethernet']=ethernet
                    if option.verbose:
                        log.debug("Ethernet: %s" % (ethernet))

                    continue

                if line.strip().startswith('uid'):
                    li = line.strip().split()
                    uid=li[1]
                    result['uid']=uid
                    if option.verbose:
                        log.debug("UID: %s" % (uid))
                    continue

                if line.strip().startswith('client-hostname'):
                    li = line.strip().split()
                    uname=li[1]
                    result['client-hostname']=uname
                    if option.verbose:
                        log.debug("Client-Hostname: %s" % (uname))
                    continue

    except KeyboardInterrupt:
        log.setLevel(logging.WARNING)
        log.warning('Program is over!')
        sql.close()
        sys.exit(1)
