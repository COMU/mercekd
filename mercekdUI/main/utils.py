from random import randint
import random, time, string, datetime
from mercekdUI.main.models import Lease, Lease_IP, Lease_Mac

def randIP():
    a = randint(1,254)
    b = randint(1,254)
    c = randint(1,254)
    d = randint(1,254)
    return '%d.%d.%d.%d' % (a,b,c,d)

def randMAC():
    mac = [ 0x00,
      randint(0x00, 0xff),
      randint(0x00, 0xff),
      randint(0x00, 0xff),
      randint(0x00, 0xff),
      randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randDate(start, end, prop):
   return strTimeProp(start, end, '%Y-%m-%d %I:%M:%S', prop)


def randName(size=randint(6,10), chars=string.ascii_uppercase):
   return ''.join(random.choice(chars) for x in range(size))

def parseLease(leases_list, status=0):
    parsed_leases_list = []
    parsed_expired_leases_list = []
    for i in range(0,len(leases_list)):
       if leases_list[i].ends > datetime.datetime.today():
         parsed_leases_list.append(leases_list[i])
       else:
         parsed_expired_leases_list.append(leases_list[i])
    if status=='active':
     return parsed_leases_list
    else:
     return parsed_expired_leases_list

def listCount(lease_list):
     count = []
     count.append(len(parseLease(lease_list,'active')))
     count.append(len(parseLease(lease_list,'0')))
     return count

def addRandomLeases():
     ## Add random 100 leases to database ##
     for i in range(0,5):
         randomnumber = random.randint(0,5)
         if  randomnumber == 1:
             Lease.objects.create(
                 ip = Lease_IP.objects.create(
                     v4 = randIP(),
                     ip_name =randName(),
                 ),
                 mac = Lease_Mac.objects.create(
                     mac = randMAC(),
                     mac_name =randName(),
                 ),
                 starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
                 ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
                 uid = randMAC(),
                 client = randName(),
                 )
         elif randomnumber == 2:
             Lease.objects.create(
                 ip = Lease_IP.objects.create(
                     v4 = randIP(),
                 ),
                 mac = Lease_Mac.objects.create(
                     mac = randMAC(),
                     mac_name =randName(),
                 ),
                 starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
                 ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
                 uid = randMAC(),
                 client = randName(),
             )
         elif randomnumber == 3:
             Lease.objects.create(
                 ip = Lease_IP.objects.create(
                     v4 = randIP(),
                     ip_name =randName(),
                 ),
                 mac = Lease_Mac.objects.create(
                     mac = randMAC(),
                 ),
                 starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
                 ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
                 uid = randMAC(),
                 client = randName(),
             )

         else:
             Lease.objects.create(
                 ip = Lease_IP.objects.create(
                     v4 = randIP(),
                     ip_name =randName(),
                 ),
                 mac = Lease_Mac.objects.create(
                     mac = randMAC(),
                 ),
                 starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
                 ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
                 uid = randMAC(),
                 client = randName(),
             )

             ### Random function ends ###

def addCustomLeases():
    Lease.objects.create(
        ip = Lease_IP.objects.create(
            v4 = "test235",
            ip_name ="test363452"
        ),
        mac = Lease_Mac.objects.create(
            mac = "test",
            mac_name="test2"
        ),
        starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
        ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
        uid = randMAC(),
        client = "test23",
    )
    Lease.objects.create(
        ip = Lease_IP.objects.create(
            v4 = "test235",
        ),
        mac = Lease_Mac.objects.create(
            mac = "test123",
        ),
        starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
        ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
        uid = randMAC(),
        client = "test214512",
    )