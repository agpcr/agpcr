import tkinter
from .. import ProbingDepth, MissingTeethToggleButton, TeethCanvas


class UpperTeethFrame(tkinter.Frame):
    def __init__(self,
                 master=None,
                 fdi_number=None,
                 on_change_missing_callback=None,
                 on_change_probing_depth_callback=None,
                 on_change_teeth_plane_callback=None):
        super().__init__(master, width=64, height=144, borderwidth=1, relief='solid')

        self.on_change_missing_callback = on_change_missing_callback
        self.on_change_probing_depth_callback = on_change_probing_depth_callback
        self.on_change_teeth_plane_callback = on_change_teeth_plane_callback

        self.fdi_number = fdi_number
        self.is_missing_teeth = False

        # PDの入力欄をまとめるフレーム
        self.pd_frame1 = ProbingDepth(master=self, on_change=self.on_change_probing_depth)
        self.pd_frame1.pack()

        # 欠損歯をトグル切り替えするボタン
        self.missing_teeth_toggle_button_frame = MissingTeethToggleButton(
            master=self,
            fdi_number=fdi_number,
            on_click=self.on_click_missing_teeth_toggle)
        self.missing_teeth_toggle_button_frame.pack()

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self, on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.teeth_canvas_frame.pack()

        # PDの入力欄をまとめるフレーム
        self.pd_frame2 = ProbingDepth(master=self, on_change=self.on_change_probing_depth)
        self.pd_frame2.pack()

    def on_click_missing_teeth_toggle(self, ev, fdi_number):
        self.is_missing_teeth = not self.is_missing_teeth

        self.teeth_canvas_frame.toggle_missing(self.is_missing_teeth)
        self.pd_frame1.toggle_missing(self.is_missing_teeth)
        self.pd_frame2.toggle_missing(self.is_missing_teeth)

        self.on_change_missing_callback(ev, self.fdi_number)

    def on_change_probing_depth(self, nm, idx, mode):
        # PDの状態が変化した際に
        # このFrameが管理しているPD入力欄の値をまとめてコールバックに引き渡す
        pd = self.get_probing_depth()
        self.on_change_probing_depth_callback(self.fdi_number, pd, self.teeth_canvas_frame.get_teeth_plane_state())
        return pd

    def on_change_teeth_plane(self, teeth_plane, color, planes):
        self.on_change_teeth_plane_callback(self.fdi_number, teeth_plane, color, planes, self.get_probing_depth())

    def get_probing_depth(self):
        return self.pd_frame1.get_values(), self.pd_frame2.get_values()

    def get_plane_state(self):
        return self.teeth_canvas_frame.get_teeth_plane_state()
