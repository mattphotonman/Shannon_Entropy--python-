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
several string lengths from nmin to nmax.
"""

import sys
from stringstat import *

#Parse input
if len(sys.argv)<2 or len(sys.argv)>4:
    print >> sys.stderr, "Usage:  entropy.py filename [nmin=1] [nmax=5]"
    exit()

filename=sys.argv[1]
nmin=1
nmax=5
if len(sys.argv)>2:
    nmin=int(sys.argv[2])
if len(sys.argv)>3:
    nmax=int(sys.argv[3])

#Create StringStat objects with n=nmin,nmin+1,...,nmax
stats=[]
for n in range(nmin,nmax+1):
    stats.append(StringStat(n))

#Main loop of the program.
#Read the lines of the file and feed them to
#each of the StringStat objects in stats using
#StringStat.AddString.
f=open(filename,'r')
for line in f:
    for stat in stats:
        stat.AddString(line)

#Have all the data now, output the results.
print "n\tNstrings\tEntropy\t\tSaturation Value\tEntropy Density\tSaturation Value"
for stat in stats:
    ent=stat.ReturnEntropy()
    N=stat.ReturnN()
    ent_saturated=log(float(N))/log(2.0)
    #ent_saturated is the value the entropy would take if each string read were unique.
    print stat.n, "\t", N, "\t\t", ent, "\t", ent_saturated, "\t\t", ent/float(stat.n), "\t", ent_saturated/float(stat.n)
