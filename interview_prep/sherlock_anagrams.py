#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# helper function to get all unique substrings
def get_all_unique_substrings(input_string,string_length,substring_length):
    # loop through string to find all substrings
    substrings = [str(sorted(input_string[start_index:start_index+substring_length])) \
        for start_index in range(string_length-substring_length+1)]
    return substrings

# helper function to find out number of anagramatic pairs
def count_anagrams(substrings,count):
    # pass substrings to substrings counter
    substrings_counter = Counter(substrings)
    for substring in substrings_counter:
        # number of anagramatic pairs is nP2 = (n)!(n-2)!/2!
        count += substrings_counter[substring]*(substrings_counter[substring]-1)/2
    return count

def sherlockAndAnagrams(s):
    count = 0
    string_length = len(s)
    # consider substrings of the same length to minimize memory requirement
    for substring_length in range(1,string_length):
        verboseprint('considering substring length {}'.format(substring_length))
        # substrings are
        substrings = get_all_unique_substrings(s,string_length,substring_length)
        verboseprint('unique substrings are')
        verboseprint(substrings)
        # update number of anagramatic pairs
        count = count_anagrams(substrings,count)
        verboseprint('count is now {}'.format(count))
    return count

if __name__ == '__main__':
    verbose = True
    verboseprint = print if verbose else lambda *a, **k: None

    s = 'ifailuhkqq'

    result = sherlockAndAnagrams(s)

    print('no of substrings is {}'.format(result))

