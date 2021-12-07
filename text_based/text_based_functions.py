#!/usr/bin/env python

"""
Created: 12/7/2021
By: NuMosaic
Last Modified: 12/7/2021

This file is a collection of functions that will be useful in implementing
a text-based game (adventure or otherwise).
"""

# IMPORTS
import os, sys
import time


# GLOBAL VARIABLES
Narrator = sys.stdout
Reader = sys.stdin
Warner = sys.stderr


# FUNCTIONS
def display_text(text, speed):
    global Narrator
    for letter in text:
        Narrator.write(letter)
        Narrator.flush()
        time.sleep(speed)
    return

def read_input():
    for line in Reader:
        if line.strip() == 'q':
            break
        display_text("You said: ", 0.1)
        display_text("\n\t", 0)
        display_text(line, 0.05)
    display_text("QUITTING...\n", 0.1)
    return

def load_story_script(filepath):
    file = open(filepath, "r")
    file_lines = file.readlines()
    file.close()
    return file_lines


# TESTING
if __name__ == "__main__":
    a = load_story_script("test.txt")
    s = 0
    for l in a:
        if '.' in l:
            s = 0.5
        else:
            s = 0.25
        display_text(l, 0.1)
        time.sleep(s)
