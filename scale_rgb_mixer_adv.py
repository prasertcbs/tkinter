from tkinter import *


def rgb_mixer():
    def on_drag(e):
        color_hex = f'#{sc[0].get():02X}{sc[1].get():02X}{sc[2].get():02X}'
        tv_color.set(color_hex)
        lbl_color["bg"] = color_hex

    root = Tk()
    root.option_add("*Font", "consolas 20")
    tv_color = StringVar()
    rgb = ['red', 'green', 'blue']
    sc = []
    for i, c in enumerate(rgb):
        Label(root, text=c, fg=c).grid(row=i, column=0, sticky="sw")
        w = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg=c)
        w.grid(row=i, column=1)
        w.set(128)
        w.bind('<B1-Motion>', on_drag)
        w.bind('<Button-1>', on_drag)
        sc.append(w)

    # Label(root, text="red", fg="red").grid(row=0, column=0, sticky="sw")
    # Label(root, text="green", fg="green").grid(row=1, column=0, sticky="sw")
    # Label(root, text="blue", fg="blue").grid(row=2, column=0, sticky="sw")
    # r = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg="red")
    # r.grid(row=0, column=1)
    # r.set(128)
    # r.bind('<B1-Motion>', on_drag)
    # r.bind('<Button-1>', on_drag)
    #
    # g = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg="green")
    # g.grid(row=1, column=1)
    # g.bind('<B1-Motion>', on_drag)
    # g.bind('<Button-1>', on_drag)
    # g.set(128)
    #
    # b = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=200, width=30, fg="blue")
    # b.grid(row=2, column=1)
    # b.set(128)
    # b.bind('<B1-Motion>', on_drag)
    # b.bind('<Button-1>', on_drag)
    lbl_color = Label(root, textvariable=tv_color)
    lbl_color.grid(row=3, columnspan=2, sticky="news")
    root.mainloop()


def rating():
    def on_drag(e):
        total = 0
        for score in sc:
            total += score.get()
        rating_score.set(f'avg. = {total / len(sc):.2f}')

    root = Tk()
    root.option_add("*Font", "consolas 20")
    rating_score = StringVar()
    criteria = ['price', 'performance', 'design', 'service', 'reliability']
    sc = []
    for i, c in enumerate(criteria):
        Label(root, text=c).grid(row=i, column=0, sticky="sw")
        w = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=200, width=30)
        w.grid(row=i, column=1)
        w.set(5)
        w.bind('<B1-Motion>', on_drag)
        w.bind('<Button-1>', on_drag)
        sc.append(w)
    lbl_color = Label(root, textvariable=rating_score, bg="gold")
    lbl_color.grid(columnspan=2, sticky="news")
    root.mainloop()


if __name__ == '__main__':
    rgb_mixer()
    # rating()
