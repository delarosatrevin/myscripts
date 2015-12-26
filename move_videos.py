#!/usr/bin/env python

import sys
import os
import shutil

topDir = os.getcwd()
videoExt = 'MOV'
videoDir = os.path.join(topDir, 'videos')

move = '--move' in sys.argv

print "Searching videos on: ", topDir

for dirname, _, filenames in os.walk(topDir):

    if dirname == videoDir:
        continue

    for f in filenames:
        if f.upper().endswith(videoExt):
            path = os.path.join(dirname, f)
            relPath = os.path.relpath(path, topDir)
            if move:
                parts = relPath.split('/')
                newF = '_'.join(parts).replace(' ', '_')
                newPath = os.path.join(videoDir, newF)
                print "Moving '%s' to '%s'" % (path, newPath)
                shutil.copy(path, newPath)
                os.remove(path)
            else:
                print relPath
