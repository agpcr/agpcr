import tkinter
from .. import ProbingDepth, MissingTeethToggleButton, TeethCanvas


class LowerTeethFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=64, height=144, borderwidth=1, relief='solid')

        # 染められる歯面を描画するCanvasの生成
        teeth_canvas_frame = TeethCanvas(master=self)
        teeth_canvas_frame.pack()

        # 欠損歯をトグル切り替えするボタン
        missing_teeth_toggle_button_frame = MissingTeethToggleButton(master=self)
        missing_teeth_toggle_button_frame.pack()

        # PDの入力欄をまとめるフレーム
        pd_frame = ProbingDepth(master=self)
        pd_frame.pack()
