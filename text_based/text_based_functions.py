#!/usr/bin/env python

# Created: 12/7/2021
# By: NuMosaic
# Last Modified: 12/7/2021

"""
This file is a collection of functions that will be useful in implementing
a text-based game (adventure or otherwise).
"""

# IMPORTS
import os, sys
import time


# FUNCTIONS
def display_text(text):
    narrator = sys.stdout
    for letter in text:
        narrator.write(letter)
        time.sleep(1)
    return

display_text("hello\n")
