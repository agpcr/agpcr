import tkinter


class MissingTeethToggleButton(tkinter.Frame):
    def __init__(self, master=None, fdi_number=None, on_click=None):
        super().__init__(master)

        button = tkinter.Button(self, text=fdi_number, fg='black', width='3', takefocus=0)
        button.bind("<Button-1>", lambda ev, fdi_number=fdi_number: on_click(ev, fdi_number))
        button.pack()
