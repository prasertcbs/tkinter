from tkinter import *


def on_click():
    # print(chk1.get(), chk2.get(), chk3.get(), chk4.get(), chk5.get(), chk6.get())
    # for i, chk in enumerate(chks):
    #     if chk.get():
    #         # print(chk.get())
    #         print(interests[i])
    lst = [interests[i] for i, chk in enumerate(chks) if chk.get()]
    # print(lst)
    print(",".join(lst))


interests = ['Music', 'Book', 'Movie', 'Photography', 'Game', 'Travel']
root = Tk()
root.option_add("*Font", "impact 30")
chks = [BooleanVar() for i in interests]
# chk1 = BooleanVar()
# chk2 = BooleanVar()
# chk3 = BooleanVar()
# chk4 = BooleanVar()
# chk5 = BooleanVar()
# chk6 = BooleanVar()
Label(root, text="Your interests", bg="gold").pack()
for i, s in enumerate(interests):
    Checkbutton(root, text=s, variable=chks[i]).pack(anchor=W)  # W = West

# Checkbutton(root, text="Music", variable=chk1).pack(anchor=W) # W = West
# Checkbutton(root, text="Book", variable=chk2).pack(anchor=W)
# Checkbutton(root, text="Movie", variable=chk3).pack(anchor=W)
# Checkbutton(root, text="Photography", variable=chk4).pack(anchor=W)
# Checkbutton(root, text="Game", variable=chk5).pack(anchor=W)
# Checkbutton(root, text="Travel", variable=chk6).pack(anchor=W)
Button(root, text="submit", command=on_click).pack()
root.mainloop()
