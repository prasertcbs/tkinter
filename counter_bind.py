from tkinter import *

# color name: https://wiki.tcl.tk/37701

# global variables
male_cnt = 0
female_cnt = 0
total_cnt = 0

# event handlers
def on_click(e):
    global male_cnt, female_cnt
    global total_cnt
    gender = e.widget["text"]
    e.widget["fg"] = "black"
    if gender == "male":
        male_cnt += 1
        tv_male.set(male_cnt)
    else:
        female_cnt += 1
        tv_female.set(female_cnt)
    total_cnt += 1
    tv_total.set(f'total = {total_cnt}')


def right_click(e):
    global male_cnt, female_cnt
    global total_cnt
    gender = e.widget["text"]
    e.widget["fg"] = "red"
    if gender == "male":
        male_cnt -= 1
        tv_male.set(male_cnt)
    else:
        female_cnt -= 1
        tv_female.set(female_cnt)
    total_cnt -= 1
    tv_total.set(f'total = {total_cnt}')


def male_click(e):
    global male_cnt
    global total_cnt
    male_cnt += 1
    total_cnt += 1
    tv_male.set(male_cnt)
    tv_total.set(f'total = {total_cnt}')


def female_click(e):
    global female_cnt
    global total_cnt
    female_cnt += 1
    total_cnt += 1
    tv_female.set(female_cnt)
    tv_total.set(f'total = {total_cnt}')

# main
root = Tk()
root.option_add("*Font", "consolas 25")

tv_male = IntVar()
tv_female = IntVar()
tv_total = StringVar()

btn_male = Button(root, text="male", bg="deep sky blue", width=8)
btn_male.grid(row=0,
              column=0,
              ipady=20)
btn_male.bind("<Button-1>", on_click)
btn_male.bind("<Button-3>", right_click)
btn_female = Button(root, text="female", bg="hot pink", width=8)
btn_female.grid(row=0,
                column=1,
                ipady=20)
btn_female.bind("<Button-1>", on_click)
btn_female.bind("<Button-3>", right_click)
Label(root, textvariable=tv_male, bg="deep sky blue").grid(row=1, column=0, sticky="news")
Label(root, textvariable=tv_female, bg="hot pink").grid(row=1, column=1, sticky="news")
Label(root, textvariable=tv_total, bg="gold").grid(row=2, columnspan=2, sticky="news")
root.mainloop()
