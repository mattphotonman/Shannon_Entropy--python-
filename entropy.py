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

#-----------------------
#Imports
#-----------------------
from math import *
from UserList import UserList
import copy
import sys
import string

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

    def AddString(self,strng):
        """Takes in a string called strng, and adds each character
        of the string using AddChar."""
        if type(strng)==str:
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
        strng=""
        for ch in strlist:
            if not(ischar(ch)):
                print >> sys.stderr, "Error:  Non char got into StringStat.queue."
                exit()
            strng+=ch

        #Now can add/increment this string in self.data
        self.Incr(strng)
        return newchar
    
    def Incr(self,key):
        """Adds key into self.data with value 1 if key isn't
        in there already.  If it is in there, it increments
        the value by 1."""
        if key in self.data:
            self.data[key]+=1
        else:
            self.data[key]=1

    def ParseChar(self,char):
        """This function decides if char should is an
        admissible character.  If not it returns None,
        if so it returns the character, but possibly
        modifies it as well.

        This function should be rewritten depending
        on the type of characters for which you want
        to gather statistics.  In this version, it
        accepts only the 26 letters and turns capitals
        into small letters."""
        if not(ischar(char)):
            print >> sys.stderr, "Error:  Tried to parse non-string or string with more than one character using StringStat.ParseChar."
            exit()

        newchar=string.lower(char)
        if newchar in string.lowercase:
            return newchar
        else:
            return None

    def ReturnEntropy(self):
        """Returns the Shannon entropy based on the frequencies
        of different strings recorded in the self.data dictionary."""

        #The quantity we wish to calculate is
        #
        #H=-\sum(p_i log(p_i) , i) = -\sum(n_i/N log(n_i/N), i)
        #
        #where i indexes the different strings, i.e. the unique keys
        #in the self.data dictionary.  Here p_i is the probability
        #of string i, estimated by p_i=n_i/N where n_i the frequency
        #of occurrence of string i, and N=\sum(n_i, i) is the total
        #number of strings examined.  n_i is the value of the key
        #in the self.data dictionary, i.e. n_i=self.data[string_i].

        entropy=0.0
        N=float(len(self.data))
        for nint in self.data.itervalues():
            ni=float(nint)
            entropy+=-ni/N*log(ni/N)
        entropy/=log(2.0)  #convert to base 2 logarithm
        return entropy

    def ReturnEntropyDensity(self):
        """Returns entropy density = H/n, where n=self.n is the length
        of strings being examined by the current object."""
        return self.ReturnEntropy()/self.n

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

