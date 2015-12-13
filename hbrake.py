#!/usr/bin/python

# This script will receive a files as argument and convert
# with HandBrakeCLI using the preset "MySmallVideo"

import os, sys;

files = sys.argv[1:];

for f in files:
    p = f.split('.')[0];
    cmd = 'HandBrakeCLI -i "%s" -o "small_%s.mp4" --preset="MySmallVideo"' % (f, p);
    os.system(cmd);
    #print f;
