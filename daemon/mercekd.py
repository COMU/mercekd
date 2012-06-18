
import os
import sys
import logging

#Options Bolumu

yardim= """

"Bu kisim yardim bolumu"""

paths="/home/halil/mercekd"

verbose="verbose kismi"

if len(sys.argv)<2:
    print "..."

elif sys.argv[1]=="-h":
    print yardim

elif sys.argv[1]=="-p":
    print paths

elif sys.argv[1]=="-v":
    print "Options:\n\n-h\tHelp\n-p\tPath\n-v\tVerbose\n"

else:
    print "Boyle bir secenek yok"

#Dosya acma bolumu
try:
    f=open("/home/halil/mercekd/daemon/leases.txt",'r')


except:
    print  "This file does not exist\n"


#tail bolumu
def tail( f, window=20 ):
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if (bytes - BUFSIZ > 0):
            # Seek back one whole BUFSIZ
            f.seek(block*BUFSIZ, 2)
            # read BUFFER
            data.append(f.read(BUFSIZ))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            data.append(f.read(bytes))
        linesFound = data[-1].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return '\n'.join(' '.join(data).splitlines()[-window:])

while True:
    try:
        tail_try=tail(f,window=7)
        find_1=tail_try.find("lease")
        find_2=tail_try.find("}",find_1)
        find_final=tail_try[find_1:find_2]
        print find_final

    except KeyboardInterrupt:
        print "\nThere is an exception"
        sys.exit(1)