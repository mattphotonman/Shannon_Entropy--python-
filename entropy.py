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

#Imports
from math import *

#Global variables

#Classes


#Main body of the code

