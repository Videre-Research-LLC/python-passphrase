#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

__author__ = "Christophe Gauge"
__email__ = "chris@videreresearch.com"
__version__ = "1.0.1"

'''

Generate a passphrase of between 2 to 5 dictionary words with random first letter
capitalization and a random number of special characters between the words.

'''


# I M P O R T S ###############################################################

import sys
import os
import random

# G L O B A L S ###############################################################

try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    script_directory = sys._MEIPASS
except Exception:
    script_directory = os.path.dirname(os.path.abspath(__file__))
dictionary_file = "american-english"
my_dictionary = os.path.join(script_directory, dictionary_file)


# F U N C T I O N S ###########################################################


def dicopen():
    """Opens the file of dictionary words as a list."""
    with open(my_dictionary) as file:
        f = file.read()
    return f.split('\n')

def genPassword(numwords):
    """Generate a new passphrase of a given number of words."""
    r = random.SystemRandom()
    # Special characters to add to the string.
    pads = '0123456789!@#$%-_+^&*()0123456789'
    words = dicopen()
    # print(len(words))
    wordlist = []
    for x in range(numwords - 1):
        # Pick a random dictionary word
        random_word = words[r.randint(0, len(words) - 1)].strip()
        # Randomly capitalize the first letter
        if bool(random.getrandbits(1)):
            random_word = random_word.capitalize()
        # Randomly add a random number of special characters after the word
        if bool(random.getrandbits(1)):
            for y in range(random.randint(0, 4)):
                random_word += pads[r.randint(0, len(pads) - 1)]
        # Randomly add a random number of special characters before the word
        if bool(random.getrandbits(1)):
            for y in range(random.randint(0, 4)):
                random_word = pads[r.randint(0, len(pads) - 1)] + random_word
        # Add the word to teh list
        wordlist.append(random_word)
    # Convert the list of words to a dash-separated string
    return '-'.join(wordlist)

def main():
    """Main function."""
    r2 = random.SystemRandom()
    # Generate a passphrase of between 2 to 5 dictionary words
    print(genPassword(r2.randint(2, 5)))

    sys.exit(0)

###############################################################################


if __name__ == "__main__":
    main()
