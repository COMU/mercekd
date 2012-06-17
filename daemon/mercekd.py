
import os
import sys

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
























