#!/usr/bin/env python
"""
Calculates the Shannon entropy (density) of a text file.
The Shannon entropy is given by

H=-\sum(p_i log(p_i) , i)

where i indexes possible states/configurations, and p_i
is the probability/frequency of that configuration.
We look at strings of length n, and thus i indexes all
strings of length n that occur in the document.  We are
interested in the entropy density, or information per
character, and thus we calculate H/n.  We do this for
several string lengths from 1 to n_max.
"""

import sys
from stringstat import *

#Parse input
if len(sys.argv)<2 or len(sys.argv)>3:
    print >> sys.stderr, "Usage:  entropy.py filename [nmax=5]"
    exit()

filename=sys.argv[1]
if len(sys.argv)==2:
    nmax=5
else:
    nmax=int(sys.argv[2])

#Create StringStat objects with n=1,2,...,nmax
stats=[]
for i in range(nmax):
    stats.append(StringStat(i+1))

#Main loop of the program.
#Read the lines of the file and feed them to
#each of the StringStat objects in stats using
#StringStat.AddString.
f=open(filename,'r')
for line in f:
    for i in range(nmax):
        stats[i].AddString(line)

#Have all the data now, output the results.
print "n\tEntropy Density"
for i in range(nmax):
    print stats[i].n, "\t", stats[i].ReturnEntropyDensity()
