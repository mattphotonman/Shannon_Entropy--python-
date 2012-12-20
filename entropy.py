#!/usr/bin/env python
"""
Calculates the Shannon entropy (density) of a text file.
The Shannon entropy is given by

H=\sum(-p_i log(p_i) , i)

where i indexes possible states/configurations, and p_i
is the probability/frequency of that configuration.
We look at strings of length n, and thus i indexes all
strings of length n that occur in the document.  We are
interested in the entropy density, or information per
character, and thus we calculate H/n.  We do this for
several string lengths from 1 to n_max.
"""

#-----------------------
#Imports
#-----------------------
from math import *
from UserList import UserList
import copy
import sys

#-----------------------
#Global variables
#-----------------------


#-----------------------
#Classes
#-----------------------

class Queue:
    """This is a special type of queue with a maximum
    size n, and with methods that are particular to the
    Shannon entropy code."""
    def __init__(self,n=1):
        self.n=n
        self.data=[]

    def Add(self,item):
        self.data.append(item)
        if len(self.data)<self.n:
            return None
        elif len(self.data)==self.n:
            return copy.copy(self.data)
        elif len(self.data)==self.n+1:
            self.data.pop(0)
            return copy.copy(self.data)
        else:
            print >> sys.stderr, "Error:  Queue became too large."
            exit()

    def __repr__(self): return repr(self.data)

#-----------------------
#Main body of the code
#-----------------------

