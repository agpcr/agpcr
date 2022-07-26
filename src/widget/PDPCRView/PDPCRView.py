import tkinter
from . import Upper, Lower


class PDPCRView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 上顎の入力UI
        upper = Upper(self)
        upper.pack()

        spacer = tkinter.Frame()
        spacer.pack(pady=10)

        lower = Lower(self)
        lower.pack()