# fill, padx, pady

from tkinter import *


def demo1():
    root = Tk()
    root.option_add("*Font", "impact 25")
    Label(root, text="mocha", bg="red").pack(side=TOP, fill=X, ipadx=20, ipady=40)
    Label(root, text="latte", bg="green").pack(side=TOP, fill=X, ipadx=20, ipady=30)
    Label(root, text="espresso", bg="blue").pack(side=TOP, fill=X, ipadx=20, ipady=20)
    root.mainloop()


def demo2():
    root = Tk()
    root.option_add("*Font", "impact 25")
    Label(root, text="mocha", bg="red").pack(side=LEFT, fill=X, ipadx=20, ipady=40,
                                             padx=10, pady=40)
    Label(root, text="latte", bg="green").pack(side=LEFT, fill=X, ipadx=20, ipady=30,
                                               padx=40)
    Label(root, text="espresso", bg="blue").pack(side=LEFT, fill=X, ipadx=20, ipady=20)
    root.mainloop()


def demo3():
    root = Tk()
    root.option_add("*Font", "impact 25")
    menus = ['mocha', 'latte', 'espresso']
    colors = ['red', 'green', 'blue']
    for i, m in enumerate(menus):
        Label(root, text=m, bg=colors[i], width=15).pack(side=LEFT, padx=10)
    root.mainloop()


if __name__ == '__main__':
    # demo1()
    # demo2()
    demo3()
