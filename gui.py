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
    endScreen = tk.Label(root, text="You win!", font="Verdana 20 bold", fg="green")
    missCounter = 1
    hitCounter = 1

    def __init__(self):
        self.root.geometry("850x600")
        self.root.resizable(0, 0)
        self.setup_pic()
        self.setup_bottom_frame()
        self.setup_restart_label()
        self.setup_buttons()
        self.root.mainloop()

    def click_btn(self, buttonChr):
        checkPic = False
        word = self.stickman.words_dict.get("a")
        wordSize = len(word)

        for i in range(0, len(self.alpha_btns)):
            if self.alpha_btns[i].cget('text') == buttonChr.upper():
                self.alpha_btns[i].config(state='disabled')

        print(len(word))
        for i in range(0, wordSize):
            if word[i] == buttonChr:
                tempLabel = self.label_vars[i]
                tempLabel.config(text=buttonChr.upper())
                self.label_vars[i] = tempLabel
                checkPic = True
                self.hitCounter += 1

        if self.hitCounter == wordSize:
            self.disable_all_buttons()
            self.endScreen.config(text="You Win!")
            self.endScreen.place(height=50, width=200, x=450, y=550)

        print(self.hitCounter)

        if not checkPic:
            if self.missCounter == 6:
                self.update_pic()
                self.disable_all_buttons()
            else:
                self.update_pic()

    # self.label.config(text=ch)
    # self.label = tk.Label(textvariable=self.label_var)

    def disable_all_buttons(self):
        for i in range(0, len(self.alpha_btns)):
            self.alpha_btns[i].config(state='disabled')

    def setup_pic(self):
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

    def update_pic(self):
        url = self.stickman.picsUrl[self.missCounter]
        response = requests.get(url)
        img_data = response.content
        self.img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        self.canvas = tk.Canvas(self.root, width=462, height=354)
        self.canvas.place(height=300, width=500, x=300, y=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.missCounter += 1

    def click_restart(self):
        self.endScreen.config(text=" ")
        self.missCounter = 0
        self.hitCounter = 1
        self.update_pic()
        self.stickman.next()
        self.label_vars.clear()
        self.setup_bottom_frame()
        self.alpha_btns.clear()
        self.setup_buttons()

    def setup_buttons(self):
        control = 1
        row = 1
        for i in range(97, 123):
            btn = tk.Button(self.root, text=(chr(i).upper()), padx=20, pady=5,
                            command=lambda m=chr(i): self.click_btn(m))
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

    def setup_bottom_frame(self):
        word = self.stickman.words_dict.get("a")
        print(word)
        print(len(word))
        sizeOfWord = len(word)
        column = 7
        for i in range(0, sizeOfWord - 1):
            tempLabel = tk.Label(self.root, text="_", pady=60, padx=10)
            if 10 < sizeOfWord < 14:
                tempLabel.config(font=("Arial", 25))
            elif 14 <= sizeOfWord < 18:
                tempLabel.config(font=("Arial", 15))
            elif 18 <= sizeOfWord < 25:
                tempLabel.config(font=("Arial", 10))
            else:
                tempLabel.config(font=("Arial", 40))

            tempLabel.grid(column=column, row=7)
            self.label_vars.append(tempLabel)
            column += 1

        # self.label = tk.Label(self.root, text="INIT", pady=60)
        # self.label.grid(column=5, row=7)

    def setup_restart_label(self):
        var = tk.StringVar()
        self.button = tk.Button(self.root, textvariable=var, command=self.click_restart)
        var.set("Restart?")
        self.button.place(height=50, width=75, x=0, y=550)
