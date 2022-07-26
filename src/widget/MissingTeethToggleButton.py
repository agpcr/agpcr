import tkinter


class MissingTeethToggleButton(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        button = tkinter.Button(self, text=18, fg='black', width='3')
        button.bind("<Button-1>", lambda ev, tooth_num=18: print(tooth_num))
        button.pack()
