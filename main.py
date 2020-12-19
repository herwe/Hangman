import tkinter as tk
from random import *

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(0, 0)
    button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow",)
    button.pack()
    with open("words.txt") as f:
        my_list = f.readlines()

    s = ""
    while len(s) <= 6:
        x = randint(1, 360000)
        s = my_list[x]

    for i in range(97, 123):
        temp = chr(i)
        #print(temp)

    print(x)
    print(s)


    #root.mainloop()
