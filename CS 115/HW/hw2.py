'''
Created on Wed Sep 18
@author:   Jonathan Joshua
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." - Jonathan Joshua

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
from dict import *
from bigdict import *
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    """takes as input a single letter string called letter and a list where each element in that list is itself a list of the form [character,value] where character is a single letter andvalue is a number associated with that letter."""
    if scorelist == []:
        return 0
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """take as input a string S and a scorelist in the format described above, which will have only lowercase letters, and should return as output the scrabble score of that string."""
    if len(S) == 0:
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def backspace(letter, list):
    """removes a letter from list"""
    if list == []:
        return []
    if list[0] == letter:
        return list[1:]
    return [list[0]] + backspace(letter, list[1:])

def inputOutput(input, list):
    """return if input can be formed by members of list"""
    if list == [] and len(input) > 0:
        return False
    elif len(input) == 0:
        return True
    if not input[0] in list:
        return False
    return inputOutput(input[1:], backspace(input[0], list))

def scoreList(Rack):
    """takes as input a Rack which is a list of lower-case letters and returns a list of all of the words in the global Dictionary that can be made from those letters and the score for each one."""
    def scoreListHelper(dict, Rack):
        if dict == []:
            return []
        if inputOutput(dict[0], Rack):
            return [[dict[0], wordScore(dict[0], scrabbleScores)]] + scoreListHelper(dict[1:], Rack)
        else:
            return scoreListHelper(dict[1:], Rack)
    return scoreListHelper(Dictionary, Rack)

def bestWord(Rack):
    """ takes as input a Rack as above and returns a list with two elements: the highest possible scoring word from that Rack followed by its score."""
    def bestWord2(score, word):
        if score == []:
            return word
        if score[0][1] >= word[1]:
            return bestWord2(score[1:], score[0])
        else:
            return bestWord2(score[1:], word)
    return bestWord2(scoreList(Rack), ['', 0])
