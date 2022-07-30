import tkinter
from . import LowerTeethFramePDPCRView, UpperTeethFramePDPCRView
from ..TeethCanvas import TeethPlane


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


        # PDPCRの表示部: 上顎の右側・左側を分けるスペーサー
        spacer6 = tkinter.Frame(self)
        spacer6.grid(row=0, column=8, padx=30)


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


        # PDPCR表示部:上下のコンポーネントのスペースを開ける
        spacer7 = tkinter.Frame(self)
        spacer7.grid(row=1, column=0, pady=10)


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
        spacer8 = tkinter.Frame(self)
        spacer8.grid(row=2, column=8, padx=30)

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
        pd_pcr_over_threshold_counter = tkinter.IntVar()
        pd_pcr_over_threshold_label_widget = tkinter.Label(self, text="PD 4mm以上の歯数")
        pd_pcr_over_threshold_label_widget.grid(row=4, column=0, columnspan=2, sticky=tkinter.W)
        pd_pcr_over_threshold_widget = tkinter.Label(self, textvariable=pd_pcr_over_threshold_counter)
        pd_pcr_over_threshold_widget.grid(row=4, column=2, sticky=tkinter.W)
        pd_pcr_over_threshold_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        pd_pcr_painted_counter = tkinter.IntVar()
        pd_pcr_painted_label_widget = tkinter.Label(self, text="プラーク歯面数")
        pd_pcr_painted_label_widget.grid(row=5, column=0, columnspan=2, sticky=tkinter.W)
        pd_pcr_painted_widget = tkinter.Label(self, textvariable=pd_pcr_painted_counter)
        pd_pcr_painted_widget.grid(row=5, column=2, sticky=tkinter.W)
        pd_pcr_painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        pd_pcr_percentage = tkinter.DoubleVar()
        pd_pcr_percentage_label_widget = tkinter.Label(self, text="agPCR割合")
        pd_pcr_percentage_label_widget.grid(row=6, column=0, columnspan=2, sticky=tkinter.W)
        pd_pcr_percentage_widget = tkinter.Label(self, textvariable=pd_pcr_percentage)
        pd_pcr_percentage_widget.grid(row=6, column=2, sticky=tkinter.W)
        pd_pcr_percentage.set(0.000)  # デフォルト値

    def on_missing(self, fdi_number):
        self.pd_pcr_views[fdi_number].on_missing()

    def on_change_probing_depth(self, fdi_number, pd, planes):
        # 閾値
        threshold = 4

        # すべてのPDがthreshold以下の場合は無条件で全歯面を
        all_under_pd_threshold_color = 'gray26'
        if (max(pd[0]) < threshold) and (max(pd[1]) < threshold):
            self.pd_pcr_views[fdi_number].paint_plane(all_under_pd_threshold_color, TeethPlane.LEFT)
            self.pd_pcr_views[fdi_number].paint_plane(all_under_pd_threshold_color, TeethPlane.TOP)
            self.pd_pcr_views[fdi_number].paint_plane(all_under_pd_threshold_color, TeethPlane.RIGHT)
            self.pd_pcr_views[fdi_number].paint_plane(all_under_pd_threshold_color, TeethPlane.BOTTOM)
            return

        # 左側の判定
        if max(pd[0][0], pd[1][0]) >= threshold and planes[TeethPlane.LEFT]:
            self.pd_pcr_views[fdi_number].paint_plane('red', TeethPlane.LEFT)
        else:
            self.pd_pcr_views[fdi_number].paint_plane('white', TeethPlane.LEFT)

        if pd[0][1] >= threshold and planes[TeethPlane.TOP]:
            self.pd_pcr_views[fdi_number].paint_plane('red', TeethPlane.TOP)
        else:
            self.pd_pcr_views[fdi_number].paint_plane('white', TeethPlane.TOP)

        if max(pd[0][2], pd[1][2]) >= threshold and planes[TeethPlane.RIGHT]:
            self.pd_pcr_views[fdi_number].paint_plane('red', TeethPlane.RIGHT)
        else:
            self.pd_pcr_views[fdi_number].paint_plane('white', TeethPlane.RIGHT)

        if pd[1][1] >= threshold and planes[TeethPlane.BOTTOM]:
            self.pd_pcr_views[fdi_number].paint_plane('red', TeethPlane.BOTTOM)
        else:
            self.pd_pcr_views[fdi_number].paint_plane('white', TeethPlane.BOTTOM)

        print((fdi_number, pd, planes))

    def on_change_teeth_plane(self, fdi_number, planes, pd):
        self.on_change_probing_depth(fdi_number, pd, planes)
        print((fdi_number, planes))
