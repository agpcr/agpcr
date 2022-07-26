import tkinter


class ProbingDepth(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # PDの入力欄の作成
        txt1 = tkinter.Entry(self, width=1)
        txt1.grid(row=0, column=0)

        txt2 = tkinter.Entry(self, width=1)
        txt2.grid(row=0, column=1)

        txt3 = tkinter.Entry(self, width=1)
        txt3.grid(row=0, column=2)

        txt4 = tkinter.Entry(self, width=1)
        txt4.grid(row=1, column=0)

        txt5 = tkinter.Entry(self, width=1)
        txt5.grid(row=1, column=1)

        txt6 = tkinter.Entry(self, width=1)
        txt6.grid(row=1, column=2)


