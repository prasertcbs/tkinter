from tkinter import *
from tkinter import ttk  # ttk -> themed tk (for Combobox)
from datetime import date


def on_click(e):
    print(cbo_day.get(), cbo_month.get(), cbo_year.get())
    mm = month_list.index(cbo_month.get()) + 1
    bd = date(int(cbo_year.get()), mm, int(cbo_day.get()))
    print(bd)


month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
              'Dec']
root = Tk()
root.option_add("*Font", "consolas 25")
cbo_day = ttk.Combobox(root, values=list(range(1, 32)), width=3, state="readonly")
cbo_day.current(0)
cbo_day.pack(side=LEFT)

cbo_month = ttk.Combobox(root, values=month_list, width=4, state="readonly")
cbo_month.current(1)
cbo_month.pack(side=LEFT)

cbo_year = ttk.Combobox(root, values=list(range(1960, 2019)), width=5)
cbo_year.current(1)
cbo_year.pack(side=LEFT)

btn = Button(root, text="submit")
btn.pack()
btn.bind("<Button-1>", on_click)

root.mainloop()
