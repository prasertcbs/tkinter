from tkinter import *

d = {"Thai": "th", "Japanese": "jp", "Korean": "kr", "Chinese": "cn", "French": "fr",
     "Australian": "au", "American": "us"}


def on_select(e):
    print(e.widget["text"], e.widget['value'])


root = Tk()
root.option_add("*Font", "consolas 20")
tv_code = StringVar()
tv_code.set("th")
n_col = 3
i = 0
for k, v in d.items():
    r = Radiobutton(root, text=k, value=v,
                    indicatoron=False,
                    width=11,
                    variable=tv_code,
                    bg="gold")
    r.bind("<Button-1>", on_select)
    # r.pack(anchor=W)
    # r.pack(anchor=W, side=LEFT)
    r.grid(row=i // n_col, column=i % n_col)
    i += 1

root.mainloop()
