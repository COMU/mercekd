#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _

class Command(BaseCommand):

  def handle(self, *args, **options):
      import logging
      import time
      import sys
      import tailer
      import os
      from datetime import datetime
      from mercekdUI.main.models import LeasesFilePath, Lease, Lease_IP, Lease_Mac, Status
      current_pid = str(os.getpid())
      current_status = Status.objects.create(status=True,
                                       pid=current_pid)
      verbosity = int(options.get('verbosity'))
      #logging
      log=logging.getLogger("mercekd")
      log.setLevel(logging.DEBUG)
      logger_console=logging.StreamHandler()
      formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
      logger_console.setFormatter(formatter)
      log.addHandler(logger_console)

      strptime = None
      if hasattr(datetime, 'strptime'):
        #python 2.6
        strptime = datetime.strptime
      else:
        #python 2.4 equivalent
        strptime = lambda date_string, format: datetime(*(time.strptime(date_string, format)[0:6]))

      leases_path = LeasesFilePath.objects.all()

      if leases_path:
          leases_path = path_list[path_list.count()-1].path
      else:
          leases_path = "/var/lib/dhcp.leases"

      log.info(_(u"mercekdaemon started. please type -h for help "))
      leases_path = "/home/faruk/leases.txt"
      try:
           if leases_path:
                 result=dict()
                 flag = False

                 for line in tailer.follow(open(leases_path)):
                    if line.startswith('lease'):
                        result.clear() # clean up result when new lease come
                        try:
                             flag = True
                             lease=line.split()
                             ip=lease[1]
                             result['ip']=ip
                             continue
                        except:
                             log.error( _(u"Unexpected error: ") + "%s" % (sys.exc_info()[0]) )
                             continue

                    if line.strip().startswith("}"):
                        log.info("IP=%s MAC=%s" % (result['ip'], result['ethernet']))
                        logger_console.flush()
                        flag = False
                        try:
                          l = Lease.objects.create(
                            ip = Lease_IP.objects.create(
                                v4 = result['ip'],
                                ),
                            mac = Lease_Mac.objects.create(
                                mac = result['ethernet'],
                                ),
                            subnetAlias = "0",
                            )
                          try:
                              l.client = result['client-hostname']
                              l.save()
                          except:
                              pass
                          try:
                              l.starts = result['start_time']
                          except:
                              pass
                          try:
                              l.ends = result['end_time']
                          except:
                              pass
                          try:
                              l.uid = result['uid']
                          except:
                              pass

                          l.save()
                        except:
                            log.error(_(u"Lease that above cannot add to database. Error: ") + "%s" % (sys.exc_info()[0]))

                    if flag:
                      if line.strip().startswith('starts'):
                        li = line.strip().split()
                        start_time=" ".join(li[2:])
                        result['start_time']=start_time
                        if verbosity>1:
                            log.debug("Start time: %s" % (start_time))
                        time_format="%Y/%m/%d %H:%M:%S;"
                        result['start_time']=strptime(start_time,time_format)
                        continue

                      if line.strip().startswith('ends'):
                        li = line.strip().split()
                        end_time=" ".join(li[2:])
                        result['end_time']=end_time
                        if verbosity>1:
                            log.debug("End time: %s" % (end_time))
                        time_format="%Y/%m/%d %H:%M:%S;"
                        result['end_time']=strptime(end_time,time_format)
                        continue

                      if line.strip().startswith('hardware'):
                        li = line.strip().split()
                        ethernet=li[2].strip(";")
                        result['ethernet']=ethernet
                        if verbosity>1:
                            log.debug("Ethernet: %s" % (ethernet))
                        continue

                      if line.strip().startswith('uid'):
                        li = line.strip().split()
                        uid=str(li[1].strip(";"))
                        result['uid']=uid
                        if verbosity>1:
                            log.debug("UID: %s" % (uid))
                        continue

                      if line.strip().startswith('client-hostname'):
                        li = line.strip().split()
                        uname=str(li[1].strip(";"))
                        result['client-hostname']=uname
                        if verbosity>1:
                            log.debug("Client-Hostname: %s" % (uname))
                        continue

      except KeyboardInterrupt:
        log.info(_(u"Goodbye :-)"))
        current_status.status = False
        current_status.save()
        sys.exit(1)

      except:
          log.error(_(u"Unexpected error: ") + "%s" % (sys.exc_info()[0]))
          current_status.status = False
          current_status.save()
          sys.exit(1)
