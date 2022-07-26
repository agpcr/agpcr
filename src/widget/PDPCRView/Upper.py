import tkinter
from .UpperTeethFrame import UpperTeethFrame


class Upper(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        margin = 5

        t18 = UpperTeethFrame(self)
        t18.grid(row=0, column=0, padx=margin)

        t17 = UpperTeethFrame(self)
        t17.grid(row=0, column=1, padx=margin)

        t16 = UpperTeethFrame(self)
        t16.grid(row=0, column=2, padx=margin)

        t15 = UpperTeethFrame(self)
        t15.grid(row=0, column=3, padx=margin)

        t14 = UpperTeethFrame(self)
        t14.grid(row=0, column=4, padx=margin)

        t13 = UpperTeethFrame(self)
        t13.grid(row=0, column=5, padx=margin)

        t12 = UpperTeethFrame(self)
        t12.grid(row=0, column=6, padx=margin)

        t11 = UpperTeethFrame(self)
        t11.grid(row=0, column=7, padx=margin)


        spacer = tkinter.Frame(self)
        spacer.grid(row=0, column=8, padx=30)


        t21 = UpperTeethFrame(self)
        t21.grid(row=0, column=9, padx=margin)

        t22 = UpperTeethFrame(self)
        t22.grid(row=0, column=10, padx=margin)

        t23 = UpperTeethFrame(self)
        t23.grid(row=0, column=11, padx=margin)

        t24 = UpperTeethFrame(self)
        t24.grid(row=0, column=12, padx=margin)

        t25 = UpperTeethFrame(self)
        t25.grid(row=0, column=13, padx=margin)

        t26 = UpperTeethFrame(self)
        t26.grid(row=0, column=14, padx=margin)

        t27 = UpperTeethFrame(self)
        t27.grid(row=0, column=15, padx=margin)

        t28 = UpperTeethFrame(self)
        t28.grid(row=0, column=16, padx=margin)
