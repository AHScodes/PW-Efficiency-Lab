"""
Password brute-force algorithm.
List of most probable passwords and english names can be found, respectively, at:
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/probable-v2-top12000.txt
- https://github.com/dominictarr/random-name/blob/master/middle-names.txt
Author: Raphael Vallat
Date: May 2018
full code: https://gist.github.com/raphaelvallat/646bd1675f2dadff09c50ebc85f298b8
Python 3
"""
import string
from itertools import product
from time import time
#from numpy import loadtxt (skipping this portion)


def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nFound Password:', ''.join(p))
            return ''.join(p)
    return False


def bruteforce(password, max_nchar=4):
    #This is a shortened version of the code
    print('Digits + ASCII lower / upper + punctuation')
    # If it fails, we start brute-forcing the 'hard' way
    # Same as possible_char = string.printable[:-5]
    all_char = string.digits + string.ascii_letters + string.punctuation

    for l in range(1, max_nchar + 1):
        #print("\t..%d char" % l)
        generator = product(all_char, repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p


# Modified start code for consistency
def start():
    print("What 4 character password are we testing?")
    pw = input()
    bruteforce(pw) 
    #print('Total time: %.2f seconds' % (end - start))

start()