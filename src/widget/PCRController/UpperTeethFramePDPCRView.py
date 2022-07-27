import tkinter
from .. import TeethCanvas


class UpperTeethFramePDPCRView(tkinter.Frame):

    def __init__(self, master=None, fdi_no=""):
        super().__init__(master)

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self)
        self.teeth_canvas_frame.pack()

        # FDI番号ラベル
        self.fdi_number_label = tkinter.Label(self, text=fdi_no)
        self.fdi_number_label.pack()
