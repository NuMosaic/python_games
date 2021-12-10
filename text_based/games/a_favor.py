#!/usr/bin/env python

"""
Created: 12/10/2021
By: NuMosaic
Last Modified: 12/10/2021

This program implements text_based_functions.py to run 
a short text-based choose-your-own adventure game.

The story is called "A Favor"
"""


# IMPORTS
from text_based_functions import *


# FUNCTIONS
def main(story_text):
    a = load_story_script(story_text)
    options = {}
    status = 0
    speed_level = 2
    player_choice = ""

    l = 0
    while l < len(a):
        s = read_markers(a[l], 2)
        if s == 2:
            end_message()
            break
        elif s == 3:
            options = parse_branch_marker(a[l])
            # to make sure the player chooses an actual option
            while player_choice not in options.keys():
                player_choice = read_player_input()
            # jump to line corresponding to choice
            l = options[player_choice]
            continue
        elif s == 4:
            player_choice = read_player_input()
        elif s == 5:
            status = narrate_story(a[l], speed_level)
        # updates
        l += 1
    return


# MAIN
if __name__ == "__main__":
    story_text = "a_favor.txt"
    main(story_text)
