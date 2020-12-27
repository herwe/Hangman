import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

from Stickman import Stickman
from Alphabuttons import Alphabuttons


class UI:
    stickman = Stickman()
    root = tk.Tk(className="Hangman")
    label = None
    label_var = tk.StringVar()
    alpha_btns = []
    label_vars = []
    img = None

    def __init__(self):
        self.root.geometry("1280x720")
        self.root.resizable(0, 0)
        self.setupPic()
        self.setupBottomFrame()
        self.setupButtons()
        self.root.mainloop()

    def clickBtn(self, buttonChr):
        word = self.stickman.words_dict.get("a")
        for i in range(0, len(self.alpha_btns)):
            if self.alpha_btns[i].cget('text') == buttonChr.upper():
                self.alpha_btns[i].config(state='disabled')
        for i in range(0, len(word)):
            if (word[i] == buttonChr):
                tempLabel = self.label_vars[i]
                tempLabel.config(text=buttonChr.upper())
                self.label_vars[i] = tempLabel

    # self.label.config(text=ch)
    # self.label = tk.Label(textvariable=self.label_var)

    def setupPic(self):
        url = "https://cdn57.androidauthority.net/wp-content/uploads/2019/04/Microsoft-Windows-11-1200x675.jpg"
        response = requests.get(url)
        img_data = response.content
        canvas = tk.Canvas(self.root, width=500, height=300)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        canvas.grid(column=18, row=18)


        #img = Image.open(url)




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
