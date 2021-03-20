from random import *


class GenerateString:
    rmdWord = None
    listWithWords = None

    def __init__(self):
        with open("words.txt") as f:
            self.listWithWords = f.readlines()

        self.next()

    def next(self):
        self.rmdWord = ""
        while len(self.rmdWord) <= 6:
            x = randint(1, 360000)
            self.rmdWord = self.listWithWords[x]
