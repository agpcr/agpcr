import tkinter


class ProbingDepth(tkinter.Frame):
    def __init__(self, master=None, on_change=None):
        super().__init__(master)

        registered_validate_cmd = master.register(self.validate)
        font_size = 10

        # PDの入力欄の作成
        self.txt1_var = tkinter.StringVar()
        self.txt1_var.trace('w', on_change)
        self.txt1 = tkinter.Entry(self,
                                  width=2,
                                  font=('', font_size),
                                  validatecommand=(registered_validate_cmd, '%S', '%P'),
                                  validate='key',
                                  textvariable=self.txt1_var)
        self.txt1.grid(row=0, column=0)

        self.txt2_var = tkinter.StringVar()
        self.txt2_var.trace('w', on_change)
        self.txt2 = tkinter.Entry(self,
                                  width=2,
                                  font=('', font_size),
                                  validatecommand=(registered_validate_cmd, '%S', '%P'),
                                  validate='key',
                                  textvariable=self.txt2_var)
        self.txt2.grid(row=0, column=1)

        self.txt3_var = tkinter.StringVar()
        self.txt3_var.trace('w', on_change)
        self.txt3 = tkinter.Entry(self,
                                  width=2,
                                  font=('', font_size),
                                  validatecommand=(registered_validate_cmd, '%S', '%P'),
                                  validate='key',
                                  textvariable=self.txt3_var)
        self.txt3.grid(row=0, column=2)

        self.txt1.bind("<Shift-Return>", self.focus_prev)
        self.txt1.bind("<Return>", self.focus_next)

        self.txt2.bind("<Shift-Return>", self.focus_prev)
        self.txt2.bind("<Return>", self.focus_next)

        self.txt3.bind("<Shift-Return>", self.focus_prev)
        self.txt3.bind("<Return>", self.focus_next)

    @staticmethod
    def focus_next(ev):
        ev.widget.tk_focusNext().focus()

    @staticmethod
    def focus_prev(ev):
        ev.widget.tk_focusPrev().focus()

    @staticmethod
    def validate(diff, prev_value):
        if not diff.encode('utf-8').isdigit():  # 半角の数値以外入力させない
            return False
        if len(prev_value) > 2:  # 2文字以上は入力させない
            return False
        return True

    def get_values(self):
        values = self.txt1_var.get(), self.txt2_var.get(), self.txt3_var.get()
        return [int(x or 0) for x in values]

    def toggle_missing(self, is_missing_teeth):
        if is_missing_teeth:
            self.txt1.config(state=tkinter.DISABLED)
            self.txt2.config(state=tkinter.DISABLED)
            self.txt3.config(state=tkinter.DISABLED)
            self.txt1_var.set('')
            self.txt2_var.set('')
            self.txt3_var.set('')
        else:
            self.txt1.config(state=tkinter.NORMAL)
            self.txt2.config(state=tkinter.NORMAL)
            self.txt3.config(state=tkinter.NORMAL)



