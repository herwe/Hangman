import tkinter as tk
from Stickman import Stickman
from Alphabuttons import Alphabuttons


class UI:
    stickman = Stickman()
    root = tk.Tk(className="Hangman")
    label = None
    label_var = tk.StringVar()
    alpha_btns = []

    def __init__(self):
        self.root.geometry("1280x720")
        self.root.resizable(0, 0)
        self.setupBottomFrame()
        self.setupButtons()
        self.root.mainloop()


    def clickBtn(self):
        print("hej")
        self.label.config(text="klickade")
        #self.label = tk.Label(textvariable=self.label_var)



    def setupButtons(self):
        control = 1
        row = 0
        for i in range(97, 123):
            btn = tk.Button(self.root, text=(chr(i).upper()), padx=20, pady=5, command=self.clickBtn)
            if i == 120:
                row = 1
                control = 10

            btn.grid(row=row, column=control, sticky='w'+'e'+'n'+'s', pady=150)
            control += 1
            self.alpha_btns.append(btn)



    def setupBottomFrame(self):
        self.label = tk.Label(self.root, text="INIT", pady=600)
        self.label.grid(column=11, row=3)


