from tkinter import *0

class window:
    def __init__(self)

window=Tk()
window.title("тест")

width=500
heigh=300
        x=666
y=333
window.geometry(f"{width}x{heigh}+{x}+{y}")
window.resizable(False, False)
window.iconbitmap("01.ico")
window.mainloop()
