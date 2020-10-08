#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    from collections import Counter
    if (Counter(note.split())-Counter(magazine.split())) == {}:
        return 'Yes'
    else: 
        return 'No'

if __name__ == '__main__':

    magazine = 'give me one grand today night'

    note = 'give one grand today'

    print(checkMagazine(magazine, note))
