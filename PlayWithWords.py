import nltk
from nltk.corpus import wordnet
from nltk.corpus import cmudict

import random

import csv

wordObjsList = []

class Movie:
    """
    An object that represents a Movie
    """
    def __init__(self, string):
        self.movieString = string #these strings are each line from movie_titles_metadata.txt
        self.convoObjsList = []
        self.charObjsList = []

class Conversation:
    """
    A conversation object contains all the dialogue of a Conversation
    """
    def __init__(self, string):
        self.conversationString = string #these strings are each line from movie_conversations.txt
        self.dialogueObjsList = []

class Character:
    """
    A character object contains all the information about a character.
    """
    def __init__(self, string):
        self.characterString = string #these strings are each line from movie_characters_metadata.txt


class Dialogue:
    """
    An object of dialogue is one spoken line
    """
    def __init__(self, string):
        self.dialogueString = string #these strings are each line from movie_lines.txt
        self.wordObjsList = []
        self.tokens = nltk.word_tokenize(dialogueString) # Tokenize each line of dialogue


class Word:
    """
    A word object is a single word from a Dialogue object.
    """
    def __init__(self, string):
        self.string = string
        self.followingWordsDict = {}
        self.antonyms = []
        self.synonyms = []

        for syn in wordnet.synsets("good"):
            for l in syn.lemmas():
                self.synonyms.append(l.name())
                if l.antonyms():
                    self.antonyms.append(l.antonyms()[0].name())

def numSyl(word):
    """
    Determine ths syllables in a word. Used for word replacement and tokenization.
    """
    try:
        syllables = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
        return syllables[0]
    except KeyError:
        return -1


def main():
