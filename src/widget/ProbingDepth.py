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

        self.txt1.bind("<Shift-Return>", self.focus_prev)
        self.txt1.bind("<Return>", self.focus_next)

        self.txt2.bind("<Shift-Return>", self.focus_prev)
        self.txt2.bind("<Return>", self.focus_next)

        self.txt3.bind("<Shift-Return>", self.focus_prev)
        self.txt3.bind("<Return>", self.focus_next)

    def focus_next(self, ev):
        ev.widget.tk_focusNext().focus()

    def focus_prev(self, ev):
        ev.widget.tk_focusPrev().focus()

    def toggle_missing(self, is_missing_teeth):
        if is_missing_teeth:
            self.txt1.config(state=tkinter.DISABLED)
            self.txt2.config(state=tkinter.DISABLED)
            self.txt3.config(state=tkinter.DISABLED)
        else:
            self.txt1.config(state=tkinter.NORMAL)
            self.txt2.config(state=tkinter.NORMAL)
            self.txt3.config(state=tkinter.NORMAL)



