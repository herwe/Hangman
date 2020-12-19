from GenerateString import GenerateString


class Stickman:
    lines = None
    words_dict = None
    rmdStr = None

    def __init__(self):
        temp = GenerateString()
        self.rmdStr = temp.rmdWord
        self.lines = 0
        for i in range(97, 123):
            self.words_dict = {chr(i): self.rmdStr}

    # def draw(self):

    def add(self):
        self.lines += 1
