#!/usr/bin/env python
# Usage: convert.py PATTERN OUTPUT_DIR [PERCENT=10]


import os, glob, sys

n = len(sys.argv)
if n < 3 or n > 5:
  print 'Usage: convert.py "PATTERN" OUTPUT_DIR [PERCENT=10] [PREFIX=img]'
  sys.exit(1)

pattern = sys.argv[1]
outdir = sys.argv[2]

if n >= 4:
  percent = int(sys.argv[3])
else:
  percent = 10
  
if n == 5:
    prefix = sys.argv[4]
else:
    prefix = 'img'

files = glob.glob(pattern)
files.sort()

for i, f in enumerate(files):
 cmd = 'convert -resize %%%d %s %s/%s%03d.jpg' % (percent, f, outdir, prefix, i+1)
 print cmd
 os.system(cmd)
