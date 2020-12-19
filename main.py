import tkinter as tk
from RandomWordGenerator import RandomWord

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(0, 0)
    button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow",)
    button.pack()
    r = RandomWord(max_word_size=5)
    print(r.generate())

    root.mainloop()
