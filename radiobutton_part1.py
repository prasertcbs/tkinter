from tkinter import *

def on_select():
    print(v_gender.get())

root = Tk()
root.option_add("*Font", "consolas 20")
v_gender = StringVar()
v_gender.set("f")

showIndicator = True
Radiobutton(root, text="male", value="m", variable=v_gender, fg="deep sky blue", indicatoron=showIndicator, command=on_select).pack(side=LEFT, padx=30)
Radiobutton(root, text="female", value="f", variable=v_gender, fg="hot pink", indicatoron=showIndicator, command=on_select).pack(side=LEFT)
root.mainloop()