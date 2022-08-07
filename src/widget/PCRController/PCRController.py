import tkinter
import tkinter.ttk as ttk
from . import UpperTeethFrame
from . import LowerTeethFrame
from ..TeethCanvas import TeethPlaneState
from decimal import Decimal, ROUND_HALF_UP


class PCRController(tkinter.Frame):
    def __init__(self,
                 master=None,
                 on_change_missing_callback=None,
                 on_change_probing_depth_callback=None,
                 on_change_teeth_plane_callback=None):
        super().__init__(master, padx=10, pady=10)

        # 歯の欠損状態が変化した際のコールバック関数
        self.on_change_missing_callback = on_change_missing_callback

        # PDの状態が変化した際のコールバック関数
        self.on_change_probing_depth_callback = on_change_probing_depth_callback

        # 歯面の状態が変化した際のコールバック関数
        self.on_change_teeth_plane_callback = on_change_teeth_plane_callback

        margin = 1

        # PCR入力部: 上顎 左の入力UI
        upper_fdi_column_map = {
            18: 0,
            17: 1,
            16: 2,
            15: 3,
            14: 4,
            13: 5,
            12: 6,
            11: 7,

            21: 9,
            22: 10,
            23: 11,
            24: 12,
            25: 13,
            26: 14,
            27: 15,
            28: 16
        }

        lower_fdi_column_map = {
            48: 0,
            47: 1,
            46: 2,
            45: 3,
            44: 4,
            43: 5,
            42: 6,
            41: 7,

            31: 9,
            32: 10,
            33: 11,
            34: 12,
            35: 13,
            36: 14,
            37: 15,
            38: 16
        }

        upper_top_pd_col_frames = {}
        for fdi_number, col in upper_fdi_column_map.items():
            pd_frame = tkinter.Frame(self)
            pd_frame.grid(row=0, column=col)
            upper_top_pd_col_frames[fdi_number] = pd_frame

        uppper_bottom_pd_col_frames = {}
        for fdi_number, col in upper_fdi_column_map.items():
            pd_frame = tkinter.Frame(self)
            pd_frame.grid(row=2, column=col)
            uppper_bottom_pd_col_frames[fdi_number] = pd_frame


        lower_top_pd_col_frames = {}
        for fdi_number, col in lower_fdi_column_map.items():
            pd_frame = tkinter.Frame(self)
            pd_frame.grid(row=4, column=col)
            lower_top_pd_col_frames[fdi_number] = pd_frame

        lower_bottom_pd_col_frames = {}
        for fdi_number, col in lower_fdi_column_map.items():
            pd_frame = tkinter.Frame(self)
            pd_frame.grid(row=6, column=col)
            lower_bottom_pd_col_frames[fdi_number] = pd_frame

        upper = [18, 17, 16, 15, 14, 13, 12, 11,  21, 22, 23, 24, 25, 26, 27, 28]
        lower = [48, 47, 46, 45, 44, 43, 42, 41,  31, 32, 33, 34, 35, 36, 37, 38]

        self.pcr_frames = {}
        for fdi_number in upper:
            teeth_frame = UpperTeethFrame(self,
                                          fdi_number=fdi_number,
                                          on_change_missing_callback=self.on_change_missing,
                                          on_change_probing_depth_callback=self.on_change_probing_depth,
                                          on_change_teeth_plane_callback=self.on_change_teeth_plane,
                                          top_pd_frame=upper_top_pd_col_frames[fdi_number],
                                          bottom_pd_frame=uppper_bottom_pd_col_frames[fdi_number])
            teeth_frame.grid(row=1, column=upper_fdi_column_map[fdi_number], padx=margin)
            self.pcr_frames[fdi_number] = teeth_frame

        # PCR入力部: 上顎の右側・左側の間に入る縦の区切り線
        separator_1 = ttk.Separator(
            self,
            style="red.TSeparator",
            orient=tkinter.VERTICAL,
        )
        separator_1.grid(row=0, column=8, rowspan=7, sticky="ns", padx=30)

        # PCR入力部: 上下のコンポーネントを分離する横の線
        separator_2 = ttk.Separator(
            self,
            style="red.TSeparator",
            orient=tkinter.VERTICAL,
        )
        separator_2.grid(row=3, column=0, columnspan=17, sticky='ew', pady=20)

        # PCR入力部: 下顎 左の入力UI
        for fdi_number in lower:
            teeth_frame = LowerTeethFrame(self,
                                          fdi_number=fdi_number,
                                          on_change_missing_callback=self.on_change_missing,
                                          on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                          on_change_teeth_plane_callback=self.on_change_teeth_plane,
                                          top_pd_frame=lower_top_pd_col_frames[fdi_number],
                                          bottom_pd_frame=lower_bottom_pd_col_frames[fdi_number])
            teeth_frame.grid(row=5, column=lower_fdi_column_map[fdi_number], padx=margin)
            self.pcr_frames[fdi_number] = teeth_frame

        # PCR入力部: 上顎の右側・左側の間に入る縦の区切り線
        # separator_3 = ttk.Separator(
        #     self,
        #     style="red.TSeparator",
        #     orient=tkinter.VERTICAL,
        # )
        # separator_3.grid(row=5, column=8, rowspan=1, sticky="ns")


        # self.pcr_frames = {
        #     18: self.t18,
        #     17: self.t17,
        #     16: self.t16,
        #     15: self.t15,
        #     14: self.t14,
        #     13: self.t13,
        #     12: self.t12,
        #     11: self.t11,
        #
        #     21: self.t21,
        #     22: self.t22,
        #     23: self.t23,
        #     24: self.t24,
        #     25: self.t25,
        #     26: self.t26,
        #     27: self.t27,
        #     28: self.t28,
        #
        #     48: self.t48,
        #     47: self.t47,
        #     46: self.t46,
        #     45: self.t45,
        #     44: self.t44,
        #     43: self.t43,
        #     42: self.t42,
        #     41: self.t41,
        #
        #     31: self.t31,
        #     32: self.t32,
        #     33: self.t33,
        #     34: self.t34,
        #     35: self.t35,
        #     36: self.t36,
        #     37: self.t37,
        #     38: self.t38,
        # }

        #####################################################
        # PCR入力部と、PDPCRの表示部を上下に分けるスペーサー
        #####################################################
        spacer4 = tkinter.Frame(self)
        spacer4.grid(row=7, column=0, pady=10)

        # 残存歯の計算結果表示
        # 残存歯のカウント表示用ラベルを作成
        self.remaining_teeth_counter = tkinter.IntVar()
        remaining_teeth_label_widget = tkinter.Label(self, text="Number of teeth present")
        remaining_teeth_label_widget.grid(row=8, column=0, columnspan=4, sticky=tkinter.W)
        remaining_teeth_widget = tkinter.Label(self, textvariable=self.remaining_teeth_counter)
        remaining_teeth_widget.grid(row=8, column=3, sticky=tkinter.W)
        self.remaining_teeth_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        self.painted_counter = tkinter.IntVar()
        painted_label_widget = tkinter.Label(self, text="Plaque-stained surfaces")
        painted_label_widget.grid(row=9, column=0, columnspan=4, sticky=tkinter.W)
        painted_widget = tkinter.Label(self, textvariable=self.painted_counter)
        painted_widget.grid(row=9, column=3, sticky=tkinter.W)
        self.painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        self.percentage = tkinter.StringVar()
        percentage_label_widget = tkinter.Label(self, text="conventional PCR")
        percentage_label_widget.grid(row=10, column=0, columnspan=4, sticky=tkinter.W)
        percentage_widget = tkinter.Label(self, textvariable=self.percentage)
        percentage_widget.grid(row=10, column=3, sticky=tkinter.W)
        self.percentage.set(str(Decimal('0.000').quantize(Decimal('0.01'), ROUND_HALF_UP)))  # デフォルト値

        # 初回計算
        missing_teeth, plaque_plane, percentage = self.aggregate_pcr()
        self.remaining_teeth_counter.set(missing_teeth)
        self.painted_counter.set(plaque_plane)
        self.percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

    def aggregate_pcr(self):
        missing_teeth = 0
        plaque_plane = 0
        plane = 0
        for frame in self.pcr_frames.values():
            # プラーク歯面をカウント
            plane_state = frame.get_plane_state()
            for state in plane_state.values():
                if state is TeethPlaneState.PLAQUE:
                    plaque_plane = plaque_plane + 1

            # 残存歯をカウント
            if not frame.is_missing_teeth:
                missing_teeth = missing_teeth + 1

                # 残存歯の歯面数をカウント
                plane = plane + len(plane_state)
        percentage = (plaque_plane / plane) * 100
        return missing_teeth, plaque_plane, percentage

    def on_change_missing(self, ev, fdi_number):
        missing_teeth, plaque_plane, percentage = self.aggregate_pcr()
        self.remaining_teeth_counter.set(missing_teeth)
        self.painted_counter.set(plaque_plane)
        self.percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

        self.on_change_missing_callback(ev, fdi_number)

    def on_change_probing_depth(self, fdi_number, pd, planes):
        missing_teeth, plaque_plane, percentage = self.aggregate_pcr()
        self.remaining_teeth_counter.set(missing_teeth)
        self.painted_counter.set(plaque_plane)
        self.percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

        self.on_change_probing_depth_callback(fdi_number, pd, planes)

    def on_change_teeth_plane(self, fdi_number, teeth_plane, next_color, planes, pd):
        missing_teeth, plaque_plane, percentage = self.aggregate_pcr()
        self.remaining_teeth_counter.set(missing_teeth)
        self.painted_counter.set(plaque_plane)
        self.percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

        self.on_change_teeth_plane_callback(fdi_number, planes, pd)