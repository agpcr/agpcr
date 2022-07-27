import tkinter
from .. import TeethCanvas


class UpperTeethFramePDPCRView(tkinter.Frame):

    def __init__(self, master=None, fdi_no=""):
        super().__init__(master)
        self.is_missing_teeth = False

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self, is_paintable=False)
        self.teeth_canvas_frame.pack()

        # FDI番号ラベル
        self.fdi_number_label = tkinter.Label(self, text=fdi_no)
        self.fdi_number_label.pack()

    def on_missing(self, ev, fdi_number):
        self.is_missing_teeth = not self.is_missing_teeth

        self.teeth_canvas_frame.toggle_missing(self.is_missing_teeth)

        # self.is_missing_callback(ev, self.fdi_number)