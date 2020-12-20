import tkinter as tk
from Stickman import Stickman


class UI:
    stickman = Stickman()
    root = tk.Tk()


    def __init__(self):
        self.root.geometry("800x600")
        self.root.resizable(0, 0)
        self.setupButtons()
        self.root.mainloop()


    def setupButtons(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT)

        btn1 = tk.Button(frame, text="A")
        btn2 = tk.Button(frame, text="B")
        btn3 = tk.Button(frame, text="C")
        btn4 = tk.Button(frame, text="D")
        btn5 = tk.Button(frame, text="E")
        btn6 = tk.Button(frame, text="F")
        btn7 = tk.Button(frame, text="G")
        btn8 = tk.Button(frame, text="H")
        btn9 = tk.Button(frame, text="I")
        btn10 = tk.Button(frame, text="J")
        btn11 = tk.Button(frame, text="K")
        btn12 = tk.Button(frame, text="L")
        btn13 = tk.Button(frame, text="M")
        btn14 = tk.Button(frame, text="N")
        btn15 = tk.Button(frame, text="O")
        btn16 = tk.Button(frame, text="P")
        btn17 = tk.Button(frame, text="Q")
        btn18 = tk.Button(frame, text="R")
        btn19 = tk.Button(frame, text="S")
        btn20 = tk.Button(frame, text="T")
        btn21 = tk.Button(frame, text="U")
        btn22 = tk.Button(frame, text="V")
        btn23 = tk.Button(frame, text="X")
        btn24 = tk.Button(frame, text="Y")
        btn25 = tk.Button(frame, text="Z")




        btn1.pack(side=tk.BOTTOM)
        btn2.pack(side=tk.BOTTOM)
        btn3.pack(side=tk.BOTTOM)
        btn4.pack(side=tk.BOTTOM)
        btn6.pack(side=tk.BOTTOM)
        btn7.pack(side=tk.BOTTOM)
        btn8.pack(side=tk.BOTTOM)
        btn9.pack(side=tk.BOTTOM)
        btn10.pack(side=tk.BOTTOM)
        btn5.pack(side=tk.BOTTOM)


