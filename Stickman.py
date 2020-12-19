import random, string

class Stickman:
    lines = None
    words_dict = None
    rmdStr = None

    def __init__(self, word):
        self.lines = 0
        for i in range(97, 123):
            self.words_dict = {chr(i): word}

    def draw(self):
        # asrad

    def add(self):
        self.lines+=1