from random import randint
import random, time, string

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


def randName(size=randint(1,10), chars=string.ascii_uppercase):
   return ''.join(random.choice(chars) for x in range(size))
   
