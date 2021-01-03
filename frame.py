from tkinter import *

root = Tk()
root.option_add("*Font", "consolas 20")
f1 = Frame(root, bg="green")
f1.grid(row=0, column=0, columnspan=2)
f2 = Frame(root, bg="red")
f2.grid(row=1, column=0)
f3 = Frame(root, bg="blue")
f3.grid(row=1, column=1, sticky="news")
Label(f1, text="this is a label", width=25).pack(padx=10, pady=10)
for menu in ['mocha', 'latte', 'espresso', 'americano', 'cappuccino']:
    Button(f2, text=menu).pack(fill=X, padx=10, pady=10)

for i, c in enumerate("1234567890"):
    Button(f3, text=c).grid(row=i // 3, column=i % 3, padx=5, pady=5)
root.mainloop()
