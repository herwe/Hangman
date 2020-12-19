import tkinter as tk
from Stickman import Stickman
from GenerateString import GenerateString


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(0, 0)
    button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow",)
    button.pack()

    test = Stickman()
    s = test.words_dict.get("d")
    print(s)



    #root.mainloop()
