from tkinter import *
# pip install Pillow qrcode
import qrcode  # https://pypi.python.org/pypi/qrcode
from PIL import Image, ImageTk


def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    return img


def demo():
    def on_click(e):
        input_text = txt.get("0.0", "end-1c") # "0.0" get text from the beginning (from first line, first character
        print(input_text)
        img = create_qrcode(input_text).resize((250, 250))
        imgTk = ImageTk.PhotoImage(img)
        qr.configure(image=imgTk)
        qr.image = imgTk

    root = Tk()
    root.title("QR code generator")
    root.option_add("*Font", "consolas 20")
    Label(root, text="enter text").grid(row=0, column=0)
    txt = Text(root, height=4, width=30, fg="green")
    txt.insert(END, "lily")
    txt.grid(row=1, column=0)
    btn = Button(root, text="create QR Code", bg="gold")
    btn.grid(row=2, column=0)
    btn.bind("<Button-1>", on_click)
    qr = Label(root) # QR Code placeholder
    qr.grid(row=0, column=1, rowspan=3)
    root.mainloop()


if __name__ == '__main__':
    # create_qrcode("lily").show()
    demo()
