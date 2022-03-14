#!/usr/bin/env python

"""
Created: 3/14/2022
By: NuMosaic
Last Modified: 3/14/2022

This python script runs a game of hangman using 
the pygames module.
"""


# IMPORTS
from random import choice


# FUNCTIONS
def readNouns(filename : str) -> list:
    """
    Parameters:
        filename : str
            name of the file to be read.
    Returns:
        lst : list
            list of the lines in the file.
    """
    file = open(filename, "r+")
    lst = file.readlines()
    return lst

def pickRandomWord(lst : list) -> str:
    """
    Parameters:
        lst : list
            a list of nouns.
    Returns:
        str
            a random noun from the list.
    """
    return choice(lst).lower()

def setupGuessing(randWord : str) -> list:
    """
    Parameters:
        randWord: str
            the random word to be guessed.
    Returns:
        temp : list
            a list of placeholder characters
            for guessing. Its length is the 
            same as randWord's.
    """
    temp = []
    for i in range(len(randWord)-1):
        temp.append("_")
    return temp

def checkInput(c : str) -> int:
    """
    Parameters:
        c : str
            the input of the player.
    Returns:
        int
            a code representing whether 
            the player inputted a correctly 
            formatted guess.
    """
    if len(c) > 1:
        return 1 # input too long
    elif c.isalpha() is not True:
        return 2 # input not a letter
    return 0

def findLetterIndices(letter : str, randWord : str) -> list[int]:
    """
    Parameters:
        letter : str
            the letter to be searched for within 
            randWord.
        randWord : str
            the word to be searched.
    Return:
        temp : list[int]
            a list of the indices where the 
            given letter was found.
    """
    temp = []
    for i in range(len(randWord)):
        if randWord[i] == letter:
            temp.append(i)
    return temp

def displayGuessing(guessTemp : list[str]) -> None:
    """
    Parameters:
        guessTemp : list[str]
            the list of what has and has not been 
            guessed.
    Returns:
        None.
    """
    for l in guessTemp:
        print(l, end=" ")
    print()
    return


# MAIN
if __name__ == "__main__":
    # setup variables
    nounList = readNouns("nouns.txt")
    secretWord = pickRandomWord(nounList)
    guesses = 5
    guessing = setupGuessing(secretWord)
    oldGuesses = set()
    guessIndices = []
    cin = ""
    
    # game loop
    while guesses > 0:
        # display guessing
        displayGuessing(guessing)
        # get player input
        cin = input("Guess a letter:\n")
        status = checkInput(cin)
        # check for errors
        while status != 0:
            if status == 1:
                print("ERROR -- input is too long!")
            elif status == 2:
                print("ERROR -- input must be letter!")
            cin = input("Guess a letter:\n")
            status = checkInput(cin)
        # check if guess was already made
        if cin in oldGuesses:
            print("You already made that guess.")
            continue # skip back to beginning
        # add guess to old guesses
        oldGuesses.add(cin)
        # check if guess is correct
        if cin in secretWord:
            guessIndices = findLetterIndices(cin, secretWord)
            # update guessing
            for ind in guessIndices:
                guessing[ind] = cin
        else:
            guesses -= 1
            print("Wrong guess. Guesses left:", guesses)
        # check for win
        if "_" not in guessing:
            print("\nCongratulations, you win!")
            break
    # Display secret word
    print("The word was:", secretWord.upper())
