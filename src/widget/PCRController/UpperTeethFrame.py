import tkinter
from .. import ProbingDepth, MissingTeethToggleButton, TeethCanvas


class UpperTeethFrame(tkinter.Frame):
    def __init__(self, master=None, fdi_number=None):
        super().__init__(master, width=64, height=144, borderwidth=1, relief='solid')
        # self.propagate(0)
        # self.grid_propagate(0)

        # PDの入力欄をまとめるフレーム
        pd_frame1 = ProbingDepth(master=self)
        pd_frame1.pack()

        # 欠損歯をトグル切り替えするボタン
        missing_teeth_toggle_button_frame = MissingTeethToggleButton(master=self, fdi_number=fdi_number, onClick=lambda ev, fdi_number=fdi_number: print(fdi_number))
        missing_teeth_toggle_button_frame.pack()

        # 染められる歯面を描画するCanvasの生成
        teeth_canvas_frame = TeethCanvas(master=self)
        teeth_canvas_frame.pack()

        # PDの入力欄をまとめるフレーム
        pd_frame2 = ProbingDepth(master=self)
        pd_frame2.pack()
