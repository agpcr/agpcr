import tkinter
from .. import TeethCanvas


class LowerTeethFramePDPCRView(tkinter.Frame):

    def __init__(self, master=None, fdi_no=""):
        super().__init__(master)

        # FDI番号ラベル
        self.fdi_number_label = tkinter.Label(self, text=fdi_no)
        self.fdi_number_label.pack()

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self, is_paintable=False)
        self.teeth_canvas_frame.pack()


