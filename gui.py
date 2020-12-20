import tkinter as tk
from Stickman import Stickman
from Alphabuttons import Alphabuttons


class UI:
    stickman = Stickman()
    root = tk.Tk(className="Hangman")
    bottomFrame = None
    alpha_btns = []

    def __init__(self):
        self.root.geometry("1280x720")
        self.root.resizable(0, 0)
        self.setupButtons()
        self.root.mainloop()

    def setupButtons(self):
        control = 1
        row = 0
        for i in range(97, 123):
            btn = tk.Button(self.root, text=(chr(i).upper()), padx=20, pady=5)
            if i == 120:
                row = 1
                control = 10

            btn.grid(row=row, column=control)
            control += 1
            self.alpha_btns.append(btn)


    def setupBottomFrame(self):


