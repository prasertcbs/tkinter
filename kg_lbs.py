# import tkinter as tk
from tkinter import *


def on_click():
    lbs = tv_kg.get() * 2.2
    tv_lbs.set(f'{lbs:.2f} lbs.')


root = Tk()
root.option_add("*Font", "impact 20")
tv_kg = DoubleVar()
tv_lbs = StringVar()

Entry(root, textvariable=tv_kg, width=7, justify="right").pack(side=LEFT, padx=10)
Label(root, text="kg.").pack(side=LEFT, padx=10)
Button(root, text=" = ", bg="green", command=on_click).pack(side=LEFT)
Label(root, textvariable=tv_lbs).pack(side=LEFT)
root.mainloop()
