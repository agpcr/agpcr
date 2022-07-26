import tkinter
from .. import TeethCanvas


class LowerTeethFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        teeth_canvas_frame = TeethCanvas(master=self)
        teeth_canvas_frame.pack()