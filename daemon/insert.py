f = file("/home/halil/mercekd/daemon/leases.txt", "a")
s = "\nlease 3.3.3.3  {" + "\n" + \
       "\t" + "starts 4 2012/06/14 13:51:44;" + "\n" + \
       "\t" + "ends 4 2012/06/14 14:51:43;" + "\n" + \
       "\t" + "hardware ethernet 00:13:e8:51:5d:e9;" + "\n" + \
"}"

print s
f.write(s)

f.close()
