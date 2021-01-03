from tkinter import *

root = Tk()
root.option_add("*Font", "consolas 20")
Button(root, text="phone", width=20).pack()
Button(root, text="camera", bg="orange").pack(fill=X)
Button(root, text="computer", fg="blue", padx=30).pack()
Button(root, text="computer", fg="blue", bd=10, width=20).pack()
Button(root, text="computer\ndisabled", fg="blue", bd=10, state=DISABLED).pack()
Button(root, text="green\ntea", fg="green", bd=10, state=NORMAL).pack()

# Button with image
# photo = PhotoImage(file="yinyang.png")
# Button(root, text="Yin Yang", image=photo).pack()
# Button(root, text="Yin Yang", image=photo, compound=LEFT).pack()
# Button(root, text="Yin Yang", image=photo, compound=LEFT, padx=20).pack()
# Button(root, text="Yin Yang", image=photo, compound=RIGHT).pack()
# Button(root, text="Yin Yang", image=photo, compound=TOP).pack()
# Button(root, text="Yin Yang", image=photo, compound=TOP, pady=20).pack()
# Button(root, text="Yin Yang", image=photo, compound=BOTTOM).pack()
root.mainloop()
