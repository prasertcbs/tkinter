from tkinter import *

# global variables
feelings = ['vd', 'd', 'n', 's', 'vs']
images = [f'{s}.png' for s in feelings]  # ['vd.png', 'd.png', ... 'vs.png']
# scores =  {'vd':0, 'd':0, 'n':0, 's':0, 'vs':0}
scores = {s: 0 for s in feelings}  # {'vd':0, 'd':0, 'n':0, 's':0, 'vs':0}

# events
def on_click(e):
    global scores
    selected = e.widget["text"]
    # print(selected)
    scores[selected] += 1
    print(scores)


root = Tk()
photos = [PhotoImage(file=img) for img in images]
for i in range(len(images)):
    btn = Button(root, image=photos[i], text=feelings[i], borderwidth=0)
    btn.pack(side=LEFT)
    btn.bind("<Button-1>", on_click)
root.mainloop()
