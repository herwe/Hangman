import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(0, 0)
    button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow",)
    button.pack()
    with open("words.txt") as f:
        my_list = f.readlines()



    #root.mainloop()
