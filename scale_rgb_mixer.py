from tkinter import *


def on_drag(e):
    color_hex = f'#{r.get():02X}{g.get():02X}{b.get():02X}'
    tv_color.set(color_hex)
    lbl_color["bg"] = color_hex


root = Tk()
root.option_add("*Font", "consolas 20")
tv_color = StringVar()
Label(root, text="red", fg="red").grid(row=0, column=0, sticky="sw")
Label(root, text="green", fg="green").grid(row=1, column=0, sticky="sw")
Label(root, text="blue", fg="blue").grid(row=2, column=0, sticky="sw")
r = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg="red")
r.grid(row=0, column=1)
r.set(128)
r.bind('<B1-Motion>', on_drag)
r.bind('<Button-1>', on_drag)

g = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg="green")
g.grid(row=1, column=1)
g.bind('<B1-Motion>', on_drag)
g.bind('<Button-1>', on_drag)
g.set(128)

b = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg="blue")
b.grid(row=2, column=1)
b.set(128)
b.bind('<B1-Motion>', on_drag)
b.bind('<Button-1>', on_drag)
lbl_color = Label(root, textvariable=tv_color)
lbl_color.grid(row=3, columnspan=2, sticky="news")
root.mainloop()
