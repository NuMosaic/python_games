#!/usr/bin/env python

"""
Created: 12/7/2021
By: NuMosaic
Last Modified: 12/7/2021

This file is a collection of functions that will be useful in implementing
a text-based game (adventure or otherwise).
"""

# IMPORTS
import sys
import time
import re


# GLOBAL VARIABLES
Narrator = sys.stdout
Reader = sys.stdin
Warner = sys.stderr

hard_punctuation = ['.', '!', '?', ';']
soft_punctuation = [',', '-', '(', ')', ':']

markers = {"branch" : "<br .*>",
        "end" : "<end>",
        "crossroads" : ("<c>", "</c>")}
crossroad = False


# CLASSES
class Character():
    """
    An object to hold the names and "talking speeds"
    of the Main Character and NPCs.
    """

    def __init__(self, 
            name : str = "Bob", 
            speeds : tuple = (0.1, 0.5, 0.8)) -> None:
        self.name = name
        self._speech_speed = speeds[0]
        self._soft_punctuation_speed = speeds[1]
        self._hard_punctuation_speed = speeds[2]
        return

    def get_name(self) -> str:
        return self.name

    def set_name(self, n : str) -> None:
        self.name = n
        return

    def get_speech_speed(self) -> float:
        return self._speech_speed

    def set_speech_speed(self, ss: float) -> None:
        self._speech_speed = ss
        return

    def get_sp_speed(self) -> float:
        return self._soft_punctuation_speed

    def set_sp_speed(self, sps: float) -> None:
        self._soft_punctuation_speed = sps
        return

    def get_hp_speed(self) -> float:
        return self._hard_punctuation_speed

    def set_hp_speed(self, hps: float) -> None:
        self._hard_punctuation_speed = hps
        return


# FUNCTIONS
def display_text(text: str,
        speaker: Character) -> None:
    """
    Parameters:
        text: string
            A string to be written to the console.
        speaker: Character
            The person that is speaking. This is so 
            that the function can access the narration
            and talking speeds of said character.

    Returns:
        None
    """
    global Narrator, hard_punctuation, soft_punctuation
    for letter in text:
        Narrator.write(letter)
        Narrator.flush()
        if letter in hard_punctuation:
            time.sleep(speaker.get_hp_speed())
        elif letter in soft_punctuation:
            time.sleep(speaker.get_sp_speed())
        else:
            time.sleep(speaker.get_speech_speed())
    return


def narrate_story(text: str,
        speed_level: int) -> int:
    """
    Parameters:
        text: string
            A string to be written to the console.
        speed_level: int
            Signifier of the display levels. 0 means 
            slow, 1 means medium, and 2 means fast.

    Returns:
         : int
            Signifies if the function ran successfully. 
            0 means success, 1 means fail.
    """
    global Narrator
    speed_list = []
    if speed_level == 0:
        speed_list = [0.16, 0.5, 0.8]
    elif speed_level == 1:
        speed_list = [0.08, 0.25, 0.5]
    elif speed_level == 2:
        speed_list = [0.04, 0.15, 0.25]
    else:
        return 1
    Nar = Character("Narrator", tuple(speed_list))
    display_text(text, Nar)
    return 0


def read_input():
    for line in Reader:
        if line.strip() == 'q':
            break
        display_text("You said: ", 0.1)
        display_text("\n\t", 0)
        display_text(line, 0.05)
    display_text("QUITTING...\n", 0.1)
    return


def load_story_script(filepath: str) -> list[str]:
    """
    Parameters:
        filepath: string
            The file path, full or relative, to the 
            text file containing the contents of the 
            story.

    Returns:
        list of strings
            The lines of the text file containing the 
            story.
    """
    file = open(filepath, "r")
    file_lines = file.readlines()
    file.close()
    return file_lines


def parse_branch_marker(line: str) -> dict:
    """
    Parameters:
        line: string
            The line with the branches marker to be 
            parsed.

    Returns:
        branches_dict: dict
            A dictionary of the choices (string) and 
            their corresponding line to jump to (int) 
            if chosen.
    """
    branches_dict = {}
    branches_list = line.strip()[:-1].split(" ")[1:]
    for opt in branches_list:
        branches = opt.split("-")
        branches_dict[branches[0]] = int(branches[1])
    return branches_dict


def end_message():
    """
    Parameters:
        None

    Returns:
        None
    """
    print("\t\t\t~~~ THE END! ~~~")
    return


def read_markers(line: str,
        speed_level: int) -> int:
    """
    Parameters:
        line: string
            The line from the story file to be 
            analyzed for markers.
        speed_level: int
            Signifier of the display levels. 0 means 
            slow, 1 means medium, and 2 means fast.

    Returns:
        status: int
            signifies whether the function ran properly. 
            0 means success, 1 means fail, 2 means 
            end the game, 3 means parse branch, 4 
            means check for player input, and 5 means 
            narrate.
    """
    global markers, crossroad
    line = line.strip()
    if line == markers["end"]: # end game
        return 2
    elif re.match(markers["branch"], line): # parse branch options
        return 3
    elif line == markers["crossroads"][0]:
        crossroad = True
    elif line == markers["crossroads"][1]: # check for player input
        crossroad = False
        return 4
    else: # narrate
        return 5
    return 0


def read_player_input() -> str:
    """
    """
    return


# TESTING
if __name__ == "__main__":
    a = load_story_script("test3.txt")
    options = {}
    start, status = 0, 0
    speed_level = 0.0
    player_choice = ''

    for l in range(start, len(a)):
        s = read_markers(a[l], 1)
        if s == 2:
            end_message()
            break
        elif s == 3:
            options = parse_branch_marker(a[l])
            # go to line player_choice corresponds to in options
        elif s == 4:
            player_choice = read_player_input()
        elif s == 5:
            status = narrate_story(a[l], speed_level)
