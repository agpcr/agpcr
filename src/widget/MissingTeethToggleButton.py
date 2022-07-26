import tkinter


class MissingTeethToggleButton(tkinter.Frame):
    def __init__(self, master=None, fdi_number=None, onClick=None):
        super().__init__(master)

        button = tkinter.Button(self, text=fdi_number, fg='black', width='3')
        button.bind("<Button-1>", onClick)
        button.pack()
