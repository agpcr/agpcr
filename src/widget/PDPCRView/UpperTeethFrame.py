import tkinter
from .. import TeethCanvas


class UpperTeethFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 染められる歯面を描画するCanvasの生成
        teeth_canvas_frame = TeethCanvas(master=self)
        teeth_canvas_frame.pack()
