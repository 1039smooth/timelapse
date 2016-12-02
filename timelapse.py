import os
import time
from datetime import datetime
import sys

d = datetime.now()

folder = str(d.month) + "." + str(d.day) + "." + str(d.year)

if os.path.isdir(folder):
        os.chdir(folder)
else:
        os.mkdir(folder)
        os.chdir(folder)

count = 0
iterations = int(raw_input("How many Photos?"))


while True:

    if count < iterations:

        d = datetime.now()
        Month = "%02d" % (d.month) 
        Day = "%02d" % (d.day)
        Year = "%04d" % (d.year)
        Hour = "%02d" % (d.hour)
        Min = "%02d" % (d.minute)
        Sec = "%02d" % (d.second)
        print "Say Cheese! ---------------------------------------->"

        os.system("fswebcam -r 1280x720 --no-banner -D 1 " + str(Hour) + ":" + str(Min) + ":" + str(Sec) + "_" + str(Month) + "." + str(Day) + "." + str(Year) + "jpg")
        #-D 1 (adds 1 sec delay)

        count += 1
        time.sleep(28)

    else:

        print " ******************************************** Exiting"
        sys.exit()
		
