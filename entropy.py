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
        """Add an item to the end and pop out the item at
        the beginning if the queue already has length n.
        If the queue has length n by the end of this,
        then return the list self.data, otherwise
        return None."""
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

class StringStat:
    """This is the main class which parses each character
    given to it and then records statistics on strings of
    length n so that the entropy for strings of length n
    can be calculated."""
    def __init__(self,n=1):
        self.n=n
        self.queue=Queue(n)
        self.data={}

    def AddString(self,string):
        """Takes in a string called string, and adds each character
        of the string using AddChar."""
        if type(string)==str:
            for char in str:
                self.AddChar(char)
        else:
            print >> sys.stderr, "Error:  Tried to add non-string using StringStat.AddString."
            exit()

    def AddChar(self,char):
        """Takes in a single character, parses it, then adds it
        to the queue if parsing didn't destroy it.  The return
        string from the queue (if any) is added or incremented
        in the self.data dictionary."""
        if not(ischar(char)):
            print >> sys.stderr, "Error:  Tried to add non-string or string with more than one character using StringStat.AddChar."
            exit()
            
        newchar=self.ParseChar(char)
        
        if not(newchar):
            #In this case char was not one of the characters
            #being accepted.  Don't add it to the queue.
            return None
        
        strlist=self.queue.Add(newchar)

        if not(strlist):
            #The queue is not up to n characters yet, so don't
            #add/increment this string in self.data.
            return newchar

        #Convert strlist from a list of chars into a string
        string=""
        for ch in strlist:
            if not(ischar(ch)):
                print >> sys.stderr, "Error:  Non char got into StringStat.queue."
                exit()
            string+=ch

        #Now can add/increment this string in self.data
        self.Incr(string)
        return newchar
    
    
        

#-----------------------
#Functions
#-----------------------

def ischar(x):
    if type(x)==str and len(x)==1:
        return True
    else:
        return False

#-----------------------
#Main body of the code
#-----------------------

