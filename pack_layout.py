from tkinter import *


def demo1():
    root = Tk()
    root.option_add("*Font", "impact 25")
    # method 1:
    Button(root, text="apple").pack(side=LEFT)
    Button(root, text="banana").pack(side=LEFT)
    Button(root, text="coconut").pack(side=LEFT)
    Button(root, text="tulip").pack(side=RIGHT)
    Button(root, text="papaya").pack(side=LEFT)

    # method 2:
    # b1 = Button(root, text="banana")
    # b1.pack(side=LEFT)
    root.mainloop()


def demo2():
    root = Tk()
    root.option_add("*Font", "impact 25")
    # method 1:
    Button(root, text="apple").pack()
    Button(root, text="banana").pack(side=BOTTOM)
    Button(root, text="coconut").pack()
    Button(root, text="tulip").pack(side=BOTTOM)
    Button(root, text="papaya").pack()

    # method 2:
    # b1 = Button(root, text="banana")
    # b1.pack(side=LEFT)
    root.mainloop()


def demo3():
    root = Tk()
    root.option_add("*Font", "impact 25")
    for c in "rainbow":
        Button(root, text=c).pack(side=BOTTOM)
    root.mainloop()


if __name__ == '__main__':
    # demo2()
    demo3()
