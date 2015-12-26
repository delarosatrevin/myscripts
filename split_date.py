#!/usr/bin/env python

import os
import sys
import time
import datetime as dt

argc = len(sys.argv);

if argc > 1:
    workPath = sys.argv[1]
else:
    print "Usage: %s DIR" % sys.argv[0]
            
for top, dirs, files in os.walk(workPath):
    for nm in files:
        fullpath = os.path.join(top, nm)
        statinfo = os.stat(fullpath)
        filesize = statinfo.st_size
        dateStr = dt.datetime.fromtimestamp(int(statinfo.st_mtime)).strftime('%Y-%m-%d')
        if not os.path.exists(dateStr):
            os.makedirs(dateStr)
        os.rename(nm, os.path.join(dateStr, nm))
                  