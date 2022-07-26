import tkinter
from .LowerTeethFrame import LowerTeethFrame


class Lower(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        margin = 5

        t18 = LowerTeethFrame(self)
        t18.grid(row=0, column=0, padx=margin)

        t17 = LowerTeethFrame(self)
        t17.grid(row=0, column=1, padx=margin)

        t16 = LowerTeethFrame(self)
        t16.grid(row=0, column=2, padx=margin)

        t15 = LowerTeethFrame(self)
        t15.grid(row=0, column=3, padx=margin)

        t14 = LowerTeethFrame(self)
        t14.grid(row=0, column=4, padx=margin)

        t13 = LowerTeethFrame(self)
        t13.grid(row=0, column=5, padx=margin)

        t12 = LowerTeethFrame(self)
        t12.grid(row=0, column=6, padx=margin)

        t11 = LowerTeethFrame(self)
        t11.grid(row=0, column=7, padx=margin)


        spacer = tkinter.Frame(self)
        spacer.grid(row=0, column=8, padx=30)


        t21 = LowerTeethFrame(self)
        t21.grid(row=0, column=9, padx=margin)

        t22 = LowerTeethFrame(self)
        t22.grid(row=0, column=10, padx=margin)

        t23 = LowerTeethFrame(self)
        t23.grid(row=0, column=11, padx=margin)

        t24 = LowerTeethFrame(self)
        t24.grid(row=0, column=12, padx=margin)

        t25 = LowerTeethFrame(self)
        t25.grid(row=0, column=13, padx=margin)

        t26 = LowerTeethFrame(self)
        t26.grid(row=0, column=14, padx=margin)

        t27 = LowerTeethFrame(self)
        t27.grid(row=0, column=15, padx=margin)

        t28 = LowerTeethFrame(self)
        t28.grid(row=0, column=16, padx=margin)