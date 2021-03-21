from GenerateString import GenerateString
from PIL import ImageTk, Image
import requests
from io import BytesIO


class Stickman:
    lines = None
    words_dict = {}
    rmdStr = None
    picsUrl = ["https://i.imgur.com/tpj2ULE.png", "https://i.imgur.com/GI679NK.png", "https://i.imgur.com/wzhJsGK.png",
               "https://i.imgur.com/o5T1IjB.png",
               "https://i.imgur.com/1iWJtaw.png", "https://i.imgur.com/4CWAWkK.png", "https://i.imgur.com/njRN5gQ.png"]
    currentImg = None


    def __init__(self):
        self.next()

    def add(self):
        self.lines += 1

    def next(self):
        temp = GenerateString()
        self.rmdStr = temp.rmdWord
        self.lines = 0
        self.words_dict.clear()
        for i in range(97, 123):
            self.words_dict[chr(i)] = self.rmdStr


