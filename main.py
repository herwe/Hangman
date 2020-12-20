import tkinter as tk
from Stickman import Stickman
from Alphabuttons import Alphabuttons
from gui import UI


def setup():
    stickman = Stickman()


if __name__ == '__main__':

    ui = UI()


    test = Stickman()
    print(test.words_dict.get("t"))



