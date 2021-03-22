import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

from Stickman import Stickman


class UI:
    stickman = Stickman()
    root = tk.Tk(className="Hangman")
    button = None
    alpha_btns = []
    label_vars = []
    img = None
    frame = None
    canvas = None
    end_screen = tk.Label(root, text="You win!", font="Verdana 20 bold", fg="green")
    miss_counter = 1
    hit_counter = 1

    def __init__(self):
        self.root.geometry("850x600")
        self.root.resizable(0, 0)
        self.setup_pic()
        self.setup_bottom_frame()
        self.setup_restart_label()
        self.setup_buttons()
        self.root.mainloop()

    def click_btn(self, button_chr):
        check_pic = False
        word = self.stickman.words_dict.get("a")
        word_size = len(word)

        for i in range(0, len(self.alpha_btns)):
            if self.alpha_btns[i].cget('text') == button_chr.upper():
                self.alpha_btns[i].config(state='disabled')

        for i in range(0, word_size):
            if word[i] == button_chr:
                temp_label = self.label_vars[i]
                temp_label.config(text=button_chr.upper())
                self.label_vars[i] = temp_label
                check_pic = True
                self.hit_counter += 1

        if self.hit_counter == word_size:
            self.disable_all_buttons()
            self.end_screen.config(text="You Win!")
            self.end_screen.place(height=50, width=200, x=450, y=550)

        if not check_pic:
            if self.miss_counter == 6:
                self.update_pic()
                self.disable_all_buttons()
            else:
                self.update_pic()

    def disable_all_buttons(self):
        for i in range(0, len(self.alpha_btns)):
            self.alpha_btns[i].config(state='disabled')

    def setup_pic(self):
        url = "https://i.imgur.com/tpj2ULE.png"
        response = requests.get(url)
        img_data = response.content
        self.img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        self.canvas = tk.Canvas(self.root, width=462, height=354)
        self.canvas.place(height=300, width=500, x=300, y=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def update_pic(self):
        url = self.stickman.picsUrl[self.miss_counter]
        response = requests.get(url)
        img_data = response.content
        self.img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        self.canvas = tk.Canvas(self.root, width=462, height=354)
        self.canvas.place(height=300, width=500, x=300, y=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.miss_counter += 1

    def click_restart(self):
        self.end_screen.config(text=" ")
        self.miss_counter = 0
        self.hit_counter = 1
        self.update_pic()
        self.destroy_labels()
        self.setup_bottom_frame()
        self.alpha_btns.clear()
        self.setup_buttons()
        self.stickman.next()

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
        size_of_word = len(word)
        column = 7
        for i in range(0, size_of_word - 1):
            temp_label = tk.Label(self.root, text="_", pady=60, padx=10)
            if 10 < size_of_word < 14:
                temp_label.config(font=("Arial", 25))
            elif 14 <= size_of_word < 18:
                temp_label.config(font=("Arial", 15))
            elif 18 <= size_of_word < 25:
                temp_label.config(font=("Arial", 10))
            else:
                temp_label.config(font=("Arial", 40))

            #temp_label.grid(column=column, row=7)
            self.label_vars.append(temp_label)
            self.label_vars[len(self.label_vars)-1].grid(column=column, row=7)
            column += 1

    def setup_restart_label(self):
        var = tk.StringVar()
        self.button = tk.Button(self.root, textvariable=var, command=self.click_restart)
        var.set("Restart?")
        self.button.place(height=50, width=75, x=0, y=550)


    def destroy_labels(self):
        for label in self.label_vars:
            label.destroy()


