from tkinter import *

def basic():
    root = Tk()
    photo = PhotoImage(file="coffee.png")
    Button(root, image=photo, borderwidth=0).pack(side=LEFT, padx=20, pady=15)
    photo_cupcake = PhotoImage(file="cupcake.png")
    Button(root, image=photo_cupcake, borderwidth=0).pack(side=LEFT, padx=20, pady=15)
    photo_burger = PhotoImage(file="burger.png")
    Button(root, image=photo_burger, borderwidth=0).pack(side=LEFT, padx=20, pady=15)

    root.mainloop()

def adv():
    images = ['coffee', 'softdrink', 'burger', 'cupcake',  'doughnut']
    root = Tk()
    photos = [PhotoImage(file=f'{img}.png') for img in images]
    for i in range(len(photos)):
        # Button(root, image=photos[i], borderwidth=0).pack(side=LEFT, padx=20, pady=15)
        Label(root, image=photos[i], borderwidth=0).pack(side=LEFT, padx=20, pady=15)

    root.mainloop()

if __name__ == '__main__':
    adv()