import tkinter


class ProbingDepth(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # PDの入力欄の作成
        self.txt1 = tkinter.Entry(self, width=1)
        self.txt1.grid(row=0, column=0)

        self.txt2 = tkinter.Entry(self, width=1)
        self.txt2.grid(row=0, column=1)

        self.txt3 = tkinter.Entry(self, width=1)
        self.txt3.grid(row=0, column=2)

        self.txt4 = tkinter.Entry(self, width=1)
        self.txt4.grid(row=1, column=0)

        self.txt5 = tkinter.Entry(self, width=1)
        self.txt5.grid(row=1, column=1)

        self.txt6 = tkinter.Entry(self, width=1)
        self.txt6.grid(row=1, column=2)

    def toggle_missing(self, is_missing_teeth):
        if is_missing_teeth:
            self.txt1.config(state=tkinter.DISABLED)
            self.txt2.config(state=tkinter.DISABLED)
            self.txt3.config(state=tkinter.DISABLED)
            self.txt4.config(state=tkinter.DISABLED)
            self.txt5.config(state=tkinter.DISABLED)
            self.txt6.config(state=tkinter.DISABLED)
        else:
            self.txt1.config(state=tkinter.NORMAL)
            self.txt2.config(state=tkinter.NORMAL)
            self.txt3.config(state=tkinter.NORMAL)
            self.txt4.config(state=tkinter.NORMAL)
            self.txt5.config(state=tkinter.NORMAL)
            self.txt6.config(state=tkinter.NORMAL)



