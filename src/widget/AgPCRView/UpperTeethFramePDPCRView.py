import tkinter
from .. import TeethCanvas


class UpperTeethFramePDPCRView(tkinter.Frame):

    def __init__(self, master=None, fdi_no="", is_under_pd=True):
        super().__init__(master, padx=9.4)
        self.is_missing_teeth = False
        self.is_under_pd = is_under_pd

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self,
                                              is_paintable=False,
                                              missing_color='gray7',
                                              under_pd_threshold_color='gray26',
                                              is_under_pd=self.is_under_pd)
        self.teeth_canvas_frame.pack()

        # FDI番号ラベル
        self.fdi_number_label = tkinter.Label(self, text=fdi_no)
        self.fdi_number_label.pack()

    def on_missing(self):
        self.is_missing_teeth = not self.is_missing_teeth
        self.teeth_canvas_frame.toggle_missing(self.is_missing_teeth)

    def set_under_pd(self, is_under_pd, position):
        self.is_under_pd = is_under_pd
        self.teeth_canvas_frame.set_under_pd(self.is_under_pd, position)

    def paint_plane(self, color, position):
        # 外部から指定のポジションの歯面を塗る
        self.teeth_canvas_frame.paint_plane(color, position)

    def get_plane_state(self):
        return self.teeth_canvas_frame.get_plane_state()
