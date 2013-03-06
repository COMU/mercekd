#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from optparse import OptionParser
from mercekdUI.main.management.commands.sql.sql import SqlManager
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import tailer
from mercekdUI.main.models import LeasesFilePath


class Command(BaseCommand):

  def handle(self, *args, **options):
  #tail
      leases_path = LeasesFilePath.objects.all()
      if leases_path:
          leases_path = path_list[path_list.count()-1].path
      else:
          leases_path = "/var/lib/dhcp.leases"

      if 1==1:
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
          #parser.add_option("-p", "--path",dest="path",help="the path of DHCP lease file",metavar="path")
          parser.add_option("-v","--verbose",dest="verbose",action='store_true',default=False)
          (option,args)=parser.parse_args()


          file_name=leases_path
          if option.verbose:
              verbose=True
          if not option.verbose:
              parser.print_help()
              sys.exit(1)

          strptime = None
          if hasattr(datetime, 'strptime'):
          #python 2.6
              strptime = datetime.strptime
          else:
          #python 2.4 equivalent
              strptime = lambda date_string, format: datetime(*(time.strptime(date_string, format)[0:6]))

          log.info("mercekd started")
          sql = SqlManager()
          sql.connect()
          try:
              if file_name:
                  result=dict()
                  flag = False
                  for line in tailer.follow(open(file_name)):
                      if line.startswith('lease'):
                          try:
                              flag = True
                              lease=line.split()
                              ip=lease[1]
                              result['ip']=ip
                              continue
                          except:
                              print "Unexpected error:", sys.exc_info()[0]
                              raise
                              ip=""
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
                              result['start_time']=strptime(start_time,time_format)
                              continue

                          if line.strip().startswith('ends'):
                              li = line.strip().split()
                              end_time=" ".join(li[2:])
                              result['end_time']=end_time
                              if option.verbose:
                                  log.debug("End time: %s" % (end_time))

                              time_format="%Y/%m/%d %H:%M:%S;"
                              result['end_time']=strptime(end_time,time_format)
                              continue

                          if line.strip().startswith('hardware'):
                              li = line.strip().split()
                              ethernet=li[2].strip(";")
                              result['ethernet']=ethernet
                              if option.verbose:
                                  log.debug("Ethernet: %s" % (ethernet))

                              continue

                          if line.strip().startswith('uid'):
                              li = line.strip().split()
                              uid=str(li[1].strip(";"))
                              result['uid']=uid
                              if option.verbose:
                                  log.debug("UID: %s" % (uid))
                              continue

                          if line.strip().startswith('client-hostname'):
                              li = line.strip().split()
                              uname=str(li[1].strip(";"))
                              result['client-hostname']=uname
                              if option.verbose:
                                  log.debug("Client-Hostname: %s" % (uname))
                              continue

          except KeyboardInterrupt:
              log.setLevel(logging.WARNING)
              log.warning('Program is over!')
              sql.close()
              sys.exit(1)