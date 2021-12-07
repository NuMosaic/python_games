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

hard_punctuation = ['.', '!', '?', ';']
soft_punctuation = [',', '-', '(', ')', ':']

markers = {"branch" : "<br .*>",
        "end" : "<end>",
        "crossroads" : ("<c>", "</c>")}


# CLASSES
class Character():
    """
    An object to hold the names and "talking speeds"
    of the Main Character and NPCs.
    """

    def __init__(self, 
            name : str = "Bob", 
            speeds : list = [0.1, 0.5, 0.8]) -> None:
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


# TESTING
if __name__ == "__main__":
    John = Character("John")
    a = load_story_script("test.txt")
    s = 0
    for l in a:
        display_text(l, John)
