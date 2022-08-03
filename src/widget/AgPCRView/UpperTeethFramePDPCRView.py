import tkinter
from .. import TeethCanvas
from ..TeethCanvas import TeethPlaneState, TeethPlane


class UpperTeethFramePDPCRView(tkinter.Frame):

    def __init__(self, master=None, fdi_no=""):
        super().__init__(master, padx=9.4)
        self.is_missing_teeth = False

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self,
                                              is_paintable=False,
                                              missing_color='gray7',
                                              under_pd_threshold_color='gray26')
        self.teeth_canvas_frame.pack()
        self.teeth_canvas_frame.set_teeth_plane_state(TeethPlane.TOP, TeethPlaneState.UNDER_PD)
        self.teeth_canvas_frame.set_teeth_plane_state(TeethPlane.RIGHT, TeethPlaneState.UNDER_PD)
        self.teeth_canvas_frame.set_teeth_plane_state(TeethPlane.BOTTOM, TeethPlaneState.UNDER_PD)
        self.teeth_canvas_frame.set_teeth_plane_state(TeethPlane.LEFT, TeethPlaneState.UNDER_PD)

        # FDI番号ラベル
        self.fdi_number_label = tkinter.Label(self, text=fdi_no)
        self.fdi_number_label.pack()

    def on_missing(self):
        self.is_missing_teeth = not self.is_missing_teeth
        self.teeth_canvas_frame.toggle_missing(self.is_missing_teeth)

    def set_teeth_plane_state(self, position, state):
        self.teeth_canvas_frame.set_teeth_plane_state(position, state)

    def get_plane_state(self):
        return self.teeth_canvas_frame.get_teeth_plane_state()

    def get_teeth_state(self):
        return self.teeth_canvas_frame.get_teeth_state()

