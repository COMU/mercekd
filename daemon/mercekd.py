#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tailer
import os
import sys
import logging
from optparse import OptionParser
import datetime

#tail
if __name__ == "__main__":

    #logging
    log=logging.getLogger("mercekd")
    log.setLevel(logging.DEBUG)
    logger_console=logging.StreamHandler()
    logger_console.setLevel(logging.DEBUG)
    formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_console.setFormatter(formatter)
    log.addHandler(logger_console)


    #options
    program='mercekd'
    parser = OptionParser(usage='usage: %prog [options] filename')
    parser.add_option("-p", "--path",type="string",action="store",dest="path", metavar='filename')
    parser.add_option("-v","--verbose",dest="verbose")
    (option,args)=parser.parse_args()

    if len(args)<1:
        parser.print_help()
        sys.exit(1)
    if option.path:
        file_name=option.path







    log.debug(datetime.datetime.now().isoformat(sep=" "))
    try:
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

                if option.verbose:
                    log.setLevel(logging.INFO)
                    log.info("Record")
                flag = False
                print "Record:", result


            if flag:
                if line.strip().startswith('starts'):
                    li = line.strip().split()
                    start_time=" ".join(li[2:])
                    result['start_time']=start_time

                    continue

                if line.strip().startswith('ends'):
                    li = line.strip().split()
                    end_time=" ".join(li[2:])
                    result['end_time']=end_time
                    continue

                if line.strip().startswith('hardware'):
                    li = line.strip().split()
                    ethernet=li[2]
                    result['ethernet']=ethernet
                    continue

                if line.strip().startswith('uid'):
                    li = line.strip().split()
                    uid=li[1]
                    result['uid']=uid
                    continue

                if line.strip().startswith('client-hostname'):
                    li = line.strip().split()
                    uname=li[1]
                    result['client-hostname']=uname
                    continue

        #line.split('\n')
    except KeyboardInterrupt:
        log.setLevel(logging.WARNING)
        log.warning('Program is over!')
        sys.exit(1)