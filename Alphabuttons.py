import tkinter as tk


class Alphabuttons:
    alpha_buttons_list = []

    def __init__(self):
        for i in range(97, 123):
            btn = tk.Button(text=(chr(i).upper()))
            self.alpha_buttons_list.append(btn)
