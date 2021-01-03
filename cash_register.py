from tkinter import *
from datetime import datetime


def record_transaction(menu_item):
    with open("sales.csv", mode='a', newline='', encoding='UTF-8') as f:
        price = menus[menu_item]
        dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f'{menu_item},{price},{dt}\n')


def show(e):
    menu_item = e.widget.cget("text")
    # print(f"menu = {menu_item}, price = {menus[menu_item]} Baht")
    tv_menu.set(f"menu = {menu_item}, price = {menus[menu_item]} Baht")
    record_transaction(menu_item)


root = Tk()
root.option_add("*Font", "impact 20")
menus = {"mocha": 30, "latte": 40, "espresso": 50, "green tea": 25, "tea": 20,
         "Thai tea": 30, "coke": 20, "water": 15, "กาแฟดำ": 25, "ชาดำเย็น": 30}
item_per_row = 2

tv_menu = StringVar()

for i, k in enumerate(menus.keys()):
    btn = Button(root, text=k, width=15)
    btn.grid(row=i // item_per_row, column=i % item_per_row)
    btn.bind("<Button-1>", show)
Label(root, text="menu", textvariable=tv_menu, fg="green").grid(columnspan=item_per_row)
root.mainloop()
