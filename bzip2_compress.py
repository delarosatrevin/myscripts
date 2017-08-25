
import os, sys

inFolder = '.'

files = os.listdir(inFolder)
files.sort()

i = 0

for f in files:
	if f.endswith('_frames.mrc'):
		i += 1
		cmd = 'bzip2 -z --best %s' % f
		print cmd
		os.system(cmd)
		
