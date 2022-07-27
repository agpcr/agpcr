import tkinter
from .. import ProbingDepth, MissingTeethToggleButton, TeethCanvas


class LowerTeethFrame(tkinter.Frame):
    def __init__(self, master=None, fdi_number=None):
        super().__init__(master, width=64, height=144, borderwidth=1, relief='solid')

        self.fdi_number = fdi_number
        self.is_missing_teeth = False

        # PDの入力欄をまとめるフレーム
        self.pd_frame1 = ProbingDepth(master=self)
        self.pd_frame1.pack()

        # 染められる歯面を描画するCanvasの生成
        self.teeth_canvas_frame = TeethCanvas(master=self)
        self.teeth_canvas_frame.pack()

        # 欠損歯をトグル切り替えするボタン
        self.missing_teeth_toggle_button_frame = MissingTeethToggleButton(master=self, fdi_number=fdi_number, onClick=self.on_click_missing_teeth_toggle)
        self.missing_teeth_toggle_button_frame.pack()

        # PDの入力欄をまとめるフレーム
        self.pd_frame2 = ProbingDepth(master=self)
        self.pd_frame2.pack()

    def on_click_missing_teeth_toggle(self, ev):
        print(self.fdi_number)
        self.is_missing_teeth = not self.is_missing_teeth

        self.teeth_canvas_frame.toggle_missing(self.is_missing_teeth)
        self.pd_frame1.toggle_missing(self.is_missing_teeth)
        self.pd_frame2.toggle_missing(self.is_missing_teeth)
