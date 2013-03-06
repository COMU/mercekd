f = file("/home/halil/mercekd/daemon/leases.txt", "a")

s = "\nlease 4.4.4.4  {" + "\n" + \
       "\t" + "starts 4 2012/06/14 13:51:44;" + "\n" + \
       "\t" + "ends 4 2012/06/14 14:51:43;" + "\n" + \
       "\t" + "hardware ethernet 00:13:e8:51:5d:e9;" + "\n" + \
       "\t" + "uid 01:f4:0b:93:03:72:12;" + "\n" +\
       "\t" + 'client-hostname "BLACKBERRY-32C";' + "\n" +\
"}"\
+\
"\nlease 1.2.3.5  {" + "\n" +\
    "\t" + "starts 4 2012/06/13 13:52:45;" + "\n" +\
    "\t" + "ends 4 2012/06/13 14:52:44;" + "\n" +\
    "\t" + "hardware ethernet 00:11:e8:51:5d:e9;" + "\n" +\
    "\t" + "uid 01:f4:0b:93:03:72:12;" + "\n" +\
    "\t" + 'client-hostname "BLACK-PC";' + "\n" +\
    "}"\
+\
"\nlease 10.42.14.127  {" + "\n" +\
    "\t" + "starts 4 2012/07/11 13:21:44;" + "\n" +\
    "\t" + "ends 4 2012/07/11 14:21:43;" + "\n" +\
    "\t" + "hardware ethernet 11:13:e8:51:22:e9;" + "\n" +\
    "\t" + "uid 54:32:0b:93:03:72:00;" + "\n" +\
    "\t" + 'client-hostname "DENEME-PC";' + "\n" +\
    "}"
s1 = "\nlease 192.44.67.250  {" + "\n" +\
     "\t" + "starts 4 2013/01/12 21:21:44;" + "\n" +\
     "\t" + "ends 4 2013/01/12 21:21:43;" + "\n" +\
     "\t" + "hardware ethernet 11:13:e0:51:e2:e9;" + "\n" +\
     "\t" + "uid 54:32:0b:93:33:21:97;" + "\n" +\
     "\t" + 'client-hostname "ORNEK-PC";' + "\n" +\
     "}"\
+\
"\nlease 168.21.17.193  {" + "\n" +\
     "\t" + "starts 4 2012/07/12 15:51:44;" + "\n" +\
     "\t" + "ends 4 2012/07/12 15:51:43;" + "\n" +\
     "\t" + "hardware ethernet 18:15:e1:61:39:b5;" + "\n" +\
     "\t" + "uid 01:00:01:6c:54:07:17;" + "\n" +\
     "\t" + 'client-hostname "THINK-PC";' + "\n" +\
     "}"\
+\
"\nlease 192.168.125.93  {" + "\n" +\
   "\t" + "starts 4 2012/07/02 12:08:43;" + "\n" +\
   "\t" + "ends 4 2012/07/02 13:08:43;" + "\n" +\
   "\t" + "hardware ethernet 00:25:11:5b:db:6d;" + "\n" +\
   "\t" + "uid 01:00:25:11:5b:db:6d;" + "\n" +\
   "\t" + 'client-hostname "ogris-4";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.222  {" + "\n" +\
   "\t" + "starts 4 2012/07/02 12:00:29;" + "\n" +\
   "\t" + "ends 4 2012/07/02 13:00:29;" + "\n" +\
   "\t" + "hardware ethernet 00:1d:e0:69:71:57;" + "\n" +\
   "\t" + "uid 01:00:1d:e0:69:71:57;" + "\n" +\
   "}"\
+\
"\nlease 192.168.125.245  {" + "\n" +\
   "\t" + "starts 1 2012/07/02 11:58:42;" + "\n" +\
   "\t" + "ends 1 2012/07/02 12:58:42;" + "\n" +\
   "\t" + "hardware ethernet 00:19:db:e8:f3:f7;" + "\n" +\
   "\t" + "uid 01:00:19:db:e8:f3:f7;" + "\n" +\
   "\t" + 'client-hostname "aidata";' + "\n" +\
   "}"
s2="\nlease 192.168.125.42  {" + "\n" +\
   "\t" + "starts 1 2012/07/02 11:52:59;" + "\n" +\
   "\t" + "ends 1 2012/07/02 12:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:01:80:68:f8:82;" + "\n" +\
   "\t" + "uid 01:00:01:80:68:f8:82;" + "\n" +\
   "\t" + 'client-hostname "OSYM";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.209  {" + "\n" +\
   "\t" + "starts 1 2012/07/02 11:50:06;" + "\n" +\
   "\t" + "ends 1 2012/07/02 12:50:06;" + "\n" +\
   "\t" + "hardware ethernet 00:19:db:c6:4e:81;" + "\n" +\
   "\t" + "uid 01:00:19:db:c6:4e:81;" + "\n" +\
   "\t" + 'client-hostname "bmyo-bali";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.25  {" + "\n" +\
   "\t" + "starts 1 2012/07/02 12:52:59;" + "\n" +\
   "\t" + "ends 1 2012/07/02 13:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:30:67:05:e8:5d;" + "\n" +\
   "\t" + "uid 01:00:30:67:05:e8:5d;" + "\n" +\
   "\t" + 'client-hostname "Ilhan-Rahmi";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.157  {" + "\n" +\
   "\t" + "starts 1 2012/07/03 14:52:59;" + "\n" +\
   "\t" + "ends 1 2012/07/03 15:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:25:11:5b:d7:3d;" + "\n" +\
   "\t" + "uid 01:00:25:11:5b:d7:3d;" + "\n" +\
   "\t" + 'client-hostname "MUDURSEKRETERI";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.200  {" + "\n" +\
   "\t" + "starts 1 2012/07/05 08:52:59;" + "\n" +\
   "\t" + "ends 1 2012/07/05 09:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:01:6c:56:05:4c;" + "\n" +\
   "}"\
+\
"\nlease 192.168.125.151  {" + "\n" +\
   "\t" + "starts 1 2012/08/02 10:52:59;" + "\n" +\
   "\t" + "ends 1 2012/08/02 11:52:59;" + "\n" +\
   "\t" + "hardware ethernet 70:f3:95:0b:e6:55;" + "\n" +\
   "\t" + 'client-hostname "hayri";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.244  {" + "\n" +\
   "\t" + "starts 4 2012/07/04 09:51:59;" + "\n" +\
   "\t" + "ends 4 2012/07/04 10:51:59;" + "\n" +\
   "\t" + "hardware ethernet 00:25:11:5b:1c:6e;" + "\n" +\
   "\t" + "uid 01:00:25:11:5b:1c:6e;" + "\n" +\
   "\t" + 'client-hostname "mud-yard";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.211  {" + "\n" +\
   "\t" + "starts 1 2012/07/11 18:52:59;" + "\n" +\
   "\t" + "ends 1 2012/07/11 19:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:01:6c:56:05:4c;" + "\n" +\
   "\t" + "uid 01:00:01:6c:56:05:4c;" + "\n" +\
   "\t" + 'client-hostname "myomuduryard";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.38  {" + "\n" +\
   "\t" + "starts 1 2012/07/21 18:52:59;" + "\n" +\
   "\t" + "ends 1 2012/07/21 19:52:59;" + "\n" +\
   "\t" + "hardware ethernet c8:0a:a9:5b:0e:ad;" + "\n" +\
   "\t" + "uid 01:c8:0a:a9:5b:0e:ad;" + "\n" +\
   "\t" + 'client-hostname "EMRE-PC";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.166  {" + "\n" +\
   "\t" + "starts 5 2012/10/02 16:52:59;" + "\n" +\
   "\t" + "ends 5 2012/10/02 17:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:30:67:05:e8:65;" + "\n" +\
   "\t" + "uid 01:00:30:67:05:e8:65;" + "\n" +\
   "\t" + 'client-hostname "bilgicik";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.41  {" + "\n" +\
   "\t" + "starts 4 2013/02/02 16:52:59;" + "\n" +\
   "\t" + "ends 4 2013/02/02 19:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:01:80:68:f8:82;" + "\n" +\
   "\t" + 'client-hostname "denemeee-PC";' + "\n" +\
   "}"\
+\
"\nlease 192.168.125.39  {" + "\n" +\
   "\t" + "starts 4 2011/09/01 09:52:59;" + "\n" +\
   "\t" + "ends 4 2011/09/01 10:52:59;" + "\n" +\
   "\t" + "hardware ethernet 00:1c:bf:5f:ae:ef;" + "\n" +\
   "\t" + "uid 01:00:1c:bf:5f:ae:ef;" + "\n" +\
   "\t" + 'client-hostname "BMYO-PC";' + "\n" +\
   "}"

#print s
print s1
#print s2



#f.write(s)
f.write(s1)
#f.write(s2)


f.flush()
