import tkinter
import tkinter.ttk as ttk
from . import LowerTeethFramePDPCRView, UpperTeethFramePDPCRView
from ..TeethCanvas import TeethPlane, TeethPlaneState, TeethState
from decimal import Decimal, ROUND_HALF_UP


class AgPCRView(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master, pady=30)

        # PDPCRの表示部: 上顎 左
        self.pd_pcr18 = UpperTeethFramePDPCRView(self, fdi_no="18")
        self.pd_pcr18.grid(row=0, column=0)

        self.pd_pcr17 = UpperTeethFramePDPCRView(self, fdi_no="17")
        self.pd_pcr17.grid(row=0, column=1)

        self.pd_pcr16 = UpperTeethFramePDPCRView(self, fdi_no="16")
        self.pd_pcr16.grid(row=0, column=2)

        self.pd_pcr15 = UpperTeethFramePDPCRView(self, fdi_no="15")
        self.pd_pcr15.grid(row=0, column=3)

        self.pd_pcr14 = UpperTeethFramePDPCRView(self, fdi_no="14")
        self.pd_pcr14.grid(row=0, column=4)

        self.pd_pcr13 = UpperTeethFramePDPCRView(self, fdi_no="13")
        self.pd_pcr13.grid(row=0, column=5)

        self.pd_pcr12 = UpperTeethFramePDPCRView(self, fdi_no="12")
        self.pd_pcr12.grid(row=0, column=6)

        self.pd_pcr11 = UpperTeethFramePDPCRView(self, fdi_no="11")
        self.pd_pcr11.grid(row=0, column=7)

        # PDPCRの表示部: 上顎の右側・左側に入る縦の区切り線
        separator_1 = ttk.Separator(
            self,
            style="red.TSeparator",
            orient=tkinter.VERTICAL,
        )
        separator_1.grid(row=0, column=8, rowspan=3, sticky="ns", padx=30)

        # PDPCR表示部: 上顎 右
        self.pd_pcr21 = UpperTeethFramePDPCRView(self, fdi_no="21")
        self.pd_pcr21.grid(row=0, column=9)

        self.pd_pcr22 = UpperTeethFramePDPCRView(self, fdi_no="22")
        self.pd_pcr22.grid(row=0, column=10)

        self.pd_pcr23 = UpperTeethFramePDPCRView(self, fdi_no="23")
        self.pd_pcr23.grid(row=0, column=11)

        self.pd_pcr24 = UpperTeethFramePDPCRView(self, fdi_no="24")
        self.pd_pcr24.grid(row=0, column=12)

        self.pd_pcr25 = UpperTeethFramePDPCRView(self, fdi_no="25")
        self.pd_pcr25.grid(row=0, column=13)

        self.pd_pcr26 = UpperTeethFramePDPCRView(self, fdi_no="26")
        self.pd_pcr26.grid(row=0, column=14)

        self.pd_pcr27 = UpperTeethFramePDPCRView(self, fdi_no="27")
        self.pd_pcr27.grid(row=0, column=15)

        self.pd_pcr28 = UpperTeethFramePDPCRView(self, fdi_no="28")
        self.pd_pcr28.grid(row=0, column=16)

        # PDPCR表示部:上下のコンポーネント分離する横の線
        separator_2 = ttk.Separator(
            self,
            style="red.TSeparator",
            orient=tkinter.VERTICAL,
        )
        separator_2.grid(row=1, column=0, columnspan=17, sticky='ew', pady=20)

        # PDPCR表示部: 下顎 左
        self.pd_pcr48 = LowerTeethFramePDPCRView(self, fdi_no="48")
        self.pd_pcr48.grid(row=2, column=0)

        self.pd_pcr47 = LowerTeethFramePDPCRView(self, fdi_no="47")
        self.pd_pcr47.grid(row=2, column=1)

        self.pd_pcr46 = LowerTeethFramePDPCRView(self, fdi_no="46")
        self.pd_pcr46.grid(row=2, column=2)

        self.pd_pcr45 = LowerTeethFramePDPCRView(self, fdi_no="45")
        self.pd_pcr45.grid(row=2, column=3)

        self.pd_pcr44 = LowerTeethFramePDPCRView(self, fdi_no="44")
        self.pd_pcr44.grid(row=2, column=4)

        self.pd_pcr43 = LowerTeethFramePDPCRView(self, fdi_no="43")
        self.pd_pcr43.grid(row=2, column=5)

        self.pd_pcr42 = LowerTeethFramePDPCRView(self, fdi_no="42")
        self.pd_pcr42.grid(row=2, column=6)

        self.pd_pcr41 = LowerTeethFramePDPCRView(self, fdi_no="41")
        self.pd_pcr41.grid(row=2, column=7)

        # 下顎の右側・左側の間に入れるスペーサー
        separator_3 = ttk.Separator(
            self,
            style="red.TSeparator",
            orient=tkinter.VERTICAL,
        )
        separator_3.grid(row=2, column=8, sticky="ns")

        self.pd_pcr31 = LowerTeethFramePDPCRView(self, fdi_no="31")
        self.pd_pcr31.grid(row=2, column=9)

        self.pd_pcr32 = LowerTeethFramePDPCRView(self, fdi_no="32")
        self.pd_pcr32.grid(row=2, column=10)

        self.pd_pcr33 = LowerTeethFramePDPCRView(self, fdi_no="33")
        self.pd_pcr33.grid(row=2, column=11)

        self.pd_pcr34 = LowerTeethFramePDPCRView(self, fdi_no="34")
        self.pd_pcr34.grid(row=2, column=12)

        self.pd_pcr35 = LowerTeethFramePDPCRView(self, fdi_no="35")
        self.pd_pcr35.grid(row=2, column=13)

        self.pd_pcr36 = LowerTeethFramePDPCRView(self, fdi_no="36")
        self.pd_pcr36.grid(row=2, column=14)

        self.pd_pcr37 = LowerTeethFramePDPCRView(self, fdi_no="37")
        self.pd_pcr37.grid(row=2, column=15)

        self.pd_pcr38 = LowerTeethFramePDPCRView(self, fdi_no="38")
        self.pd_pcr38.grid(row=2, column=16)

        self.pd_pcr_views = {
            18: self.pd_pcr18,
            17: self.pd_pcr17,
            16: self.pd_pcr16,
            15: self.pd_pcr15,
            14: self.pd_pcr14,
            13: self.pd_pcr13,
            12: self.pd_pcr12,
            11: self.pd_pcr11,

            21: self.pd_pcr21,
            22: self.pd_pcr22,
            23: self.pd_pcr23,
            24: self.pd_pcr24,
            25: self.pd_pcr25,
            26: self.pd_pcr26,
            27: self.pd_pcr27,
            28: self.pd_pcr28,

            48: self.pd_pcr48,
            47: self.pd_pcr47,
            46: self.pd_pcr46,
            45: self.pd_pcr45,
            44: self.pd_pcr44,
            43: self.pd_pcr43,
            42: self.pd_pcr42,
            41: self.pd_pcr41,

            31: self.pd_pcr31,
            32: self.pd_pcr32,
            33: self.pd_pcr33,
            34: self.pd_pcr34,
            35: self.pd_pcr35,
            36: self.pd_pcr36,
            37: self.pd_pcr37,
            38: self.pd_pcr38,
        }


        # PDPCR表示部:下部のサマリー表示部と上下を分けるセパレータ
        spacer9 = tkinter.Frame(self)
        spacer9.grid(row=3, column=0, pady=10)


        # PD4mm以上の歯数の計算結果表示
        # 残存歯のカウント表示用ラベルを作成
        self.pd_pcr_over_threshold_counter = tkinter.IntVar()
        pd_pcr_over_threshold_label_widget = tkinter.Label(self, text='Surfaces with PD≧4')
        pd_pcr_over_threshold_label_widget.grid(row=4, column=0, columnspan=4, sticky=tkinter.W)
        pd_pcr_over_threshold_widget = tkinter.Label(self, textvariable=self.pd_pcr_over_threshold_counter)
        pd_pcr_over_threshold_widget.grid(row=4, column=3, sticky=tkinter.W)
        self.pd_pcr_over_threshold_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        self.pd_pcr_painted_counter = tkinter.IntVar()
        pd_pcr_painted_label_widget = tkinter.Label(self, text="Plaque-stained surfaces with PD≧4")
        pd_pcr_painted_label_widget.grid(row=5, column=0, columnspan=4, sticky=tkinter.W)
        pd_pcr_painted_widget = tkinter.Label(self, textvariable=self.pd_pcr_painted_counter)
        pd_pcr_painted_widget.grid(row=5, column=3, sticky=tkinter.W)
        self.pd_pcr_painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        self.pd_pcr_percentage = tkinter.StringVar()
        pd_pcr_percentage_label_widget = tkinter.Label(self, text="agPCR")
        pd_pcr_percentage_label_widget.grid(row=6, column=0, columnspan=4, sticky=tkinter.W)
        pd_pcr_percentage_widget = tkinter.Label(self, textvariable=self.pd_pcr_percentage)
        pd_pcr_percentage_widget.grid(row=6, column=3, sticky=tkinter.W)
        self.pd_pcr_percentage.set(str(Decimal(0).quantize(Decimal('0.01'), ROUND_HALF_UP)))  # デフォルト値

        # 初回計算
        over_pd_planes, plaque_plane, percentage = self.aggregate_pd_pcr()
        self.pd_pcr_over_threshold_counter.set(over_pd_planes)
        self.pd_pcr_painted_counter.set(plaque_plane)
        self.pd_pcr_percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

    def aggregate_pd_pcr(self):
        over_pd_planes = 0
        plaque_plane = 0
        for frame in self.pd_pcr_views.values():
            # 欠損歯は除外する
            teeth_state = frame.get_teeth_state()
            if teeth_state is TeethState.NORMAL:
                plane_state = frame.get_plane_state()
                for state in plane_state.values():
                    # PD 4mm以上の歯面数をカウント
                    if state is TeethPlaneState.NORMAL or state is TeethPlaneState.PLAQUE:
                        over_pd_planes = over_pd_planes + 1

                    # プラーク歯面数をカウント
                    if state is TeethPlaneState.PLAQUE:
                        plaque_plane = plaque_plane + 1
        try:
            percentage = (plaque_plane / over_pd_planes) * 100
        except ZeroDivisionError:
            percentage = 0
        return over_pd_planes, plaque_plane, percentage

    def on_change_missing(self, fdi_number):
        self.pd_pcr_views[fdi_number].on_missing()

        over_pd_planes, plaque_plane, percentage = self.aggregate_pd_pcr()
        self.pd_pcr_over_threshold_counter.set(over_pd_planes)
        self.pd_pcr_painted_counter.set(plaque_plane)
        self.pd_pcr_percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

    def on_change_probing_depth(self, fdi_number, pd, planes):
        # 閾値
        threshold = 4

        # 左側の判定
        if max(pd[0][0], pd[1][0]) >= threshold and planes[TeethPlane.LEFT] is TeethPlaneState.PLAQUE:
            # PD4mm以上、プラーク(+)→赤表示
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.LEFT, TeethPlaneState.PLAQUE)
        elif max(pd[0][0], pd[1][0]) >= threshold and planes[TeethPlane.LEFT] is TeethPlaneState.NORMAL:
            # PD4mm以上、プラーク（ー）→白表示
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.LEFT, TeethPlaneState.NORMAL)
        else:
            # PD4mm未満→全てグレー
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.LEFT, TeethPlaneState.UNDER_PD)

        # 上側の判定
        if pd[0][1] >= threshold and planes[TeethPlane.TOP] is TeethPlaneState.PLAQUE:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.TOP, TeethPlaneState.PLAQUE)
        elif pd[0][1] >= threshold and planes[TeethPlane.TOP] is TeethPlaneState.NORMAL:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.TOP, TeethPlaneState.NORMAL)
        else:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.TOP, TeethPlaneState.UNDER_PD)

        # 右側の判定
        if max(pd[0][2], pd[1][2]) >= threshold and planes[TeethPlane.RIGHT] is TeethPlaneState.PLAQUE:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.RIGHT, TeethPlaneState.PLAQUE)
        elif max(pd[0][2], pd[1][2]) >= threshold and planes[TeethPlane.RIGHT] is TeethPlaneState.NORMAL:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.RIGHT, TeethPlaneState.NORMAL)
        else:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.RIGHT, TeethPlaneState.UNDER_PD)

        # 下側の判定
        if pd[1][1] >= threshold and planes[TeethPlane.BOTTOM] is TeethPlaneState.PLAQUE:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.BOTTOM, TeethPlaneState.PLAQUE)
        elif pd[1][1] >= threshold and planes[TeethPlane.BOTTOM] is TeethPlaneState.NORMAL:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.BOTTOM, TeethPlaneState.NORMAL)
        else:
            self.pd_pcr_views[fdi_number].set_teeth_plane_state(TeethPlane.BOTTOM, TeethPlaneState.UNDER_PD)

        # すべてのPDがthreshold以下の場合は無条件で全歯面を閾値以下表示状態にする
        # if (max(pd[0]) < threshold) and (max(pd[1]) < threshold):
        #     self.pd_pcr_views[fdi_number].set_under_pd(True, TeethPlane.LEFT)
        #     self.pd_pcr_views[fdi_number].set_under_pd(True, TeethPlane.TOP)
        #     self.pd_pcr_views[fdi_number].set_under_pd(True, TeethPlane.RIGHT)
        #     self.pd_pcr_views[fdi_number].set_under_pd(True, TeethPlane.BOTTOM)
        over_pd_planes, plaque_plane, percentage = self.aggregate_pd_pcr()
        self.pd_pcr_over_threshold_counter.set(over_pd_planes)
        self.pd_pcr_painted_counter.set(plaque_plane)
        self.pd_pcr_percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))

        print((fdi_number, pd, planes))

    def on_change_teeth_plane(self, fdi_number, planes, pd):
        self.on_change_probing_depth(fdi_number, pd, planes)

        over_pd_planes, plaque_plane, percentage = self.aggregate_pd_pcr()
        self.pd_pcr_over_threshold_counter.set(over_pd_planes)
        self.pd_pcr_painted_counter.set(plaque_plane)
        self.pd_pcr_percentage.set(str(Decimal(percentage).quantize(Decimal('0.01'), ROUND_HALF_UP)))
        print((fdi_number, planes))
