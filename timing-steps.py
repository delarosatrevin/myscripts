#!/usr/bin/env python

"""
Compute the time elapsed between steps of a given protocol.

Input:
    - steps.sqlite file
    - Step name to be computed (e.g., processMovie)
"""

import os, glob, sys
from datetime import datetime

from pyworkflow.protocol import StepSet


sqliteFn = sys.argv[1]
stepName = sys.argv[2]

stepSet = StepSet(filename=sqliteFn)
stepList = [step.clone() for step in stepSet if step.funcName == stepName]


timeList = [step.getElapsedTime().seconds
            for step in stepList if step.getElapsedTime().seconds > 0]

if not stepList:
    print "No steps matched with name '%s'" % stepName
    print "Select one of the followings: "
    possibleNames = []
    for step in stepSet:
        name = step.funcName.get()
        if name not in possibleNames:
            possibleNames.append(name)
    print '\n'.join(possibleNames)
    # Print different steps names

else:
    print "Matched steps: ", len(stepList)
    print "Timing: "
    #print "total (last - first): ", gettime(-1) - gettime(0)
    print "  min: ", min(timeList)
    print "  max: ", max(timeList)
    print "  avg: ", sum(timeList) / float(len(timeList))
    print " list: ", timeList

stepSet.close() # Close the connection
