import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

from Stickman import Stickman


class UI:
    stickman = Stickman()
    root = tk.Tk(className="Hangman")
    button = None
    label_var = tk.StringVar()
    alpha_btns = []
    label_vars = []
    img = None
    frame = None
    canvas = None
    newImg = None
    counter = 1

    def __init__(self):
        self.root.geometry("850x600")
        self.root.resizable(0, 0)
        self.setupPic()
        self.setupBottomFrame()
        self.setupRestartLabel()
        self.setupButtons()
        self.root.mainloop()

    def clickBtn(self, buttonChr):
        checkPic = False
        word = self.stickman.words_dict.get("a")
        for i in range(0, len(self.alpha_btns)):
            if self.alpha_btns[i].cget('text') == buttonChr.upper():
                self.alpha_btns[i].config(state='disabled')

        for i in range(0, len(word)):
            if word[i] == buttonChr:
                tempLabel = self.label_vars[i]
                tempLabel.config(text=buttonChr.upper())
                self.label_vars[i] = tempLabel
                checkPic = True

        if not checkPic:
            self.updatePic()

    # self.label.config(text=ch)
    # self.label = tk.Label(textvariable=self.label_var)

    def setupPic(self):
        # self.frame = tk.Frame(self.root, borderwidth=0, padx=0, pady=0)
        # self.frame.grid(column=1, row=1)
        # self.frame.place(bordermode=tk.INSIDE, height=100, width=100)
        url = "https://i.imgur.com/tpj2ULE.png"
        response = requests.get(url)
        img_data = response.content
        self.img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        self.canvas = tk.Canvas(self.root, width=462, height=354)
        self.canvas.place(height=300, width=500, x=300, y=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def updatePic(self):
        url = self.stickman.picsUrl[self.counter]
        response = requests.get(url)
        img_data = response.content
        self.img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        self.canvas = tk.Canvas(self.root, width=462, height=354)
        self.canvas.place(height=300, width=500, x=300, y=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.counter += 1


    def clickRestart(self):
        self.counter = 0
        self.updatePic()
        self.stickman.next()
        self.label_vars.clear()
        self.setupBottomFrame()
        self.alpha_btns.clear()
        self.setupButtons()


    def setupButtons(self):
        control = 1
        row = 1
        for i in range(97, 123):
            btn = tk.Button(self.root, text=(chr(i).upper()), padx=20, pady=5,
                            command=lambda m=chr(i): self.clickBtn(m))
            if i == 102:
                row = 2
                control = 1
            elif i == 107:
                row = 3
                control = 1
            elif i == 112:
                row = 4
                control = 1
            elif i == 117:
                row = 5
                control = 1
            elif i == 122:
                row = 6
                control = 1

            btn.grid(row=row, column=control, pady=15)
            control += 1
            self.alpha_btns.append(btn)

    def setupBottomFrame(self):
        word = self.stickman.words_dict.get("a")
        print(word)
        print(len(word))
        sizeOfWord = len(word)
        column = 7
        for i in range(0, sizeOfWord - 1):
            tempLabel = tk.Label(self.root, text="_", pady=60, padx=10)
            if 10 < sizeOfWord < 14:
                print("ett")
                tempLabel.config(font=("Arial", 25))
            elif 14 <= sizeOfWord < 18:
                print("tva")
                tempLabel.config(font=("Arial", 15))
            elif 18 <= sizeOfWord < 25:
                tempLabel.config(font=("Arial", 10))
            else:
                tempLabel.config(font=("Arial", 40))
                print("tre")

            tempLabel.grid(column=column, row=7)
            self.label_vars.append(tempLabel)
            column += 1

        # self.label = tk.Label(self.root, text="INIT", pady=60)
        # self.label.grid(column=5, row=7)

    def setupRestartLabel(self):
        var = tk.StringVar()
        self.button = tk.Button(self.root, textvariable=var, command=self.clickRestart)
        var.set("Restart?")
        self.button.place(height=50, width=75, x=0, y=550)





