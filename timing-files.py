#!/usr/bin/env python

"""
Compute the time elapsed between files.
Useful to have some statistics in processes that generates files
per iterations.
"""

import os, glob, sys
from datetime import datetime

files = sys.argv[1:]

timeDict = {}

for f in files:
    ts = os.path.getmtime(f)
    dt = datetime.fromtimestamp(ts)
    timeDict[f] = dt

# Sort files by time
files.sort(key=lambda f: timeDict[f])

def gettime(index):
    """ Return the time for a given index, corresponding to a file. """
    return timeDict[files[index]]

timeList = []

for i, f in enumerate(files):
    if i > 0:
        td = gettime(i) - gettime(i-1)
        timeList.append(td.seconds)
        if td.seconds < 3:
            print "Warning: ", i, f

    #print f, timeDict[f]

print "Matched files: ", len(files)
print "Timing: "
print "total (last - first): ", gettime(-1) - gettime(0)
print "  min: ", min(timeList)
print "  max: ", max(timeList)
print "  avg: ", sum(timeList) / float(len(timeList))
print " list: ", timeList

