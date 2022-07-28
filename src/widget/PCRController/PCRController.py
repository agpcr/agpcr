import tkinter
from . import UpperTeethFrame
from . import LowerTeethFrame
from . import UpperTeethFramePDPCRView
from . import LowerTeethFramePDPCRView


class PCRController(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        margin = 5

        # PCR入力部: 上顎 左の入力UI
        t18 = UpperTeethFrame(self, fdi_number=18)
        t18.grid(row=0, column=0, padx=margin)

        t17 = UpperTeethFrame(self, fdi_number=17)
        t17.grid(row=0, column=1, padx=margin)

        t16 = UpperTeethFrame(self, fdi_number=16)
        t16.grid(row=0, column=2, padx=margin)

        t15 = UpperTeethFrame(self, fdi_number=15)
        t15.grid(row=0, column=3, padx=margin)

        t14 = UpperTeethFrame(self, fdi_number=14)
        t14.grid(row=0, column=4, padx=margin)

        t13 = UpperTeethFrame(self, fdi_number=13)
        t13.grid(row=0, column=5, padx=margin)

        t12 = UpperTeethFrame(self, fdi_number=12)
        t12.grid(row=0, column=6, padx=margin)

        t11 = UpperTeethFrame(self, fdi_number=11)
        t11.grid(row=0, column=7, padx=margin)


        # PCR入力部: 上顎の右側・左側の間に入るスペーサー
        spacer1 = tkinter.Frame(self)
        spacer1.grid(row=0, column=8, padx=30)


        # PCR入力部: 上顎 右の入力UI
        t21 = UpperTeethFrame(self, fdi_number=21)
        t21.grid(row=0, column=9, padx=margin)

        t22 = UpperTeethFrame(self, fdi_number=22)
        t22.grid(row=0, column=10, padx=margin)

        t23 = UpperTeethFrame(self, fdi_number=23)
        t23.grid(row=0, column=11, padx=margin)

        t24 = UpperTeethFrame(self, fdi_number=24)
        t24.grid(row=0, column=12, padx=margin)

        t25 = UpperTeethFrame(self, fdi_number=25)
        t25.grid(row=0, column=13, padx=margin)

        t26 = UpperTeethFrame(self, fdi_number=26)
        t26.grid(row=0, column=14, padx=margin)

        t27 = UpperTeethFrame(self, fdi_number=27)
        t27.grid(row=0, column=15, padx=margin)

        t28 = UpperTeethFrame(self, fdi_number=28)
        t28.grid(row=0, column=16, padx=margin)



        # PCR入力部: 上下のコンポーネントのスペースを開ける
        spacer2 = tkinter.Frame(self)
        spacer2.grid(row=1, column=0, pady=10)



        # PCR入力部: 下顎 左の入力UI
        t48 = LowerTeethFrame(self, fdi_number=48)
        t48.grid(row=2, column=0, padx=margin)

        t47 = LowerTeethFrame(self, fdi_number=47)
        t47.grid(row=2, column=1, padx=margin)

        t46 = LowerTeethFrame(self, fdi_number=46)
        t46.grid(row=2, column=2, padx=margin)

        t45 = LowerTeethFrame(self, fdi_number=45)
        t45.grid(row=2, column=3, padx=margin)

        t44 = LowerTeethFrame(self, fdi_number=44)
        t44.grid(row=2, column=4, padx=margin)

        t43 = LowerTeethFrame(self, fdi_number=43)
        t43.grid(row=2, column=5, padx=margin)

        t42 = LowerTeethFrame(self, fdi_number=42)
        t42.grid(row=2, column=6, padx=margin)

        t41 = LowerTeethFrame(self, fdi_number=41)
        t41.grid(row=2, column=7, padx=margin)


        # PCR入力部: 下顎の右側・左側の間に入れるスペーサー
        spacer3 = tkinter.Frame(self)
        spacer3.grid(row=2, column=8, padx=30)


        # PCR入力部: 下顎 右の入力UI
        t31 = LowerTeethFrame(self, fdi_number=31)
        t31.grid(row=2, column=9, padx=margin)

        t32 = LowerTeethFrame(self, fdi_number=32)
        t32.grid(row=2, column=10, padx=margin)

        t33 = LowerTeethFrame(self, fdi_number=33)
        t33.grid(row=2, column=11, padx=margin)

        t34 = LowerTeethFrame(self, fdi_number=34)
        t34.grid(row=2, column=12, padx=margin)

        t35 = LowerTeethFrame(self, fdi_number=35)
        t35.grid(row=2, column=13, padx=margin)

        t36 = LowerTeethFrame(self, fdi_number=36)
        t36.grid(row=2, column=14, padx=margin)

        t37 = LowerTeethFrame(self, fdi_number=37)
        t37.grid(row=2, column=15, padx=margin)

        t38 = LowerTeethFrame(self, fdi_number=38)
        t38.grid(row=2, column=16, padx=margin)

        #####################################################
        # PCR入力部と、PDPCRの表示部を上下に分けるスペーサー
        #####################################################
        spacer4 = tkinter.Frame(self)
        spacer4.grid(row=3, column=0, pady=10)

        # 残存歯の計算結果表示
        # 残存歯のカウント表示用ラベルを作成
        remaining_teeth_counter = tkinter.IntVar()
        remaining_teeth_label_widget = tkinter.Label(self, text="残存歯")
        remaining_teeth_label_widget.grid(row=4, column=0, columnspan=2, sticky=tkinter.W)
        remaining_teeth_widget = tkinter.Label(self, textvariable=remaining_teeth_counter)
        remaining_teeth_widget.grid(row=4, column=2, sticky=tkinter.W)
        remaining_teeth_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        painted_counter = tkinter.IntVar()
        painted_label_widget = tkinter.Label(self, text="プラーク面数")
        painted_label_widget.grid(row=5, column=0, columnspan=2, sticky=tkinter.W)
        painted_widget = tkinter.Label(self, textvariable=painted_counter)
        painted_widget.grid(row=5, column=2, sticky=tkinter.W)
        painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        percentage = tkinter.DoubleVar()
        percentage_label_widget = tkinter.Label(self, text="割合")
        percentage_label_widget.grid(row=6, column=0, columnspan=2, sticky=tkinter.W)
        percentage_widget = tkinter.Label(self, textvariable=percentage)
        percentage_widget.grid(row=6, column=2, sticky=tkinter.W)
        percentage.set(0.000)  # デフォルト値


        # PDPCR表示部:上下のコンポーネントのスペースを開ける
        spacer5 = tkinter.Frame(self)
        spacer5.grid(row=7, column=0, pady=30)

        # PDPCRの表示部: 上顎 左
        pd_pcr18 = UpperTeethFramePDPCRView(self, fdi_no="18")
        pd_pcr18.grid(row=8, column=0)

        pd_pcr17 = UpperTeethFramePDPCRView(self, fdi_no="17")
        pd_pcr17.grid(row=8, column=1)

        pd_pcr16 = UpperTeethFramePDPCRView(self, fdi_no="16")
        pd_pcr16.grid(row=8, column=2)

        pd_pcr15 = UpperTeethFramePDPCRView(self, fdi_no="15")
        pd_pcr15.grid(row=8, column=3)

        pd_pcr14 = UpperTeethFramePDPCRView(self, fdi_no="14")
        pd_pcr14.grid(row=8, column=4)

        pd_pcr13 = UpperTeethFramePDPCRView(self, fdi_no="13")
        pd_pcr13.grid(row=8, column=5)

        pd_pcr12 = UpperTeethFramePDPCRView(self, fdi_no="12")
        pd_pcr12.grid(row=8, column=6)

        pd_pcr11 = UpperTeethFramePDPCRView(self, fdi_no="11")
        pd_pcr11.grid(row=8, column=7)


        # PDPCRの表示部: 上顎の右側・左側を分けるスペーサー
        spacer6 = tkinter.Frame(self)
        spacer6.grid(row=8, column=8, padx=30)


        # PDPCR表示部: 上顎 右
        pd_pcr21 = UpperTeethFramePDPCRView(self, fdi_no="21")
        pd_pcr21.grid(row=8, column=9)

        pd_pcr22 = UpperTeethFramePDPCRView(self, fdi_no="22")
        pd_pcr22.grid(row=8, column=10)

        pd_pcr23 = UpperTeethFramePDPCRView(self, fdi_no="23")
        pd_pcr23.grid(row=8, column=11)

        pd_pcr24 = UpperTeethFramePDPCRView(self, fdi_no="24")
        pd_pcr24.grid(row=8, column=12)

        pd_pcr25 = UpperTeethFramePDPCRView(self, fdi_no="25")
        pd_pcr25.grid(row=8, column=13)

        pd_pcr26 = UpperTeethFramePDPCRView(self, fdi_no="26")
        pd_pcr26.grid(row=8, column=14)

        pd_pcr27 = UpperTeethFramePDPCRView(self, fdi_no="27")
        pd_pcr27.grid(row=8, column=15)

        pd_pcr28 = UpperTeethFramePDPCRView(self, fdi_no="28")
        pd_pcr28.grid(row=8, column=16)


        # PDPCR表示部:上下のコンポーネントのスペースを開ける
        spacer7 = tkinter.Frame(self)
        spacer7.grid(row=9, column=0, pady=10)


        # PDPCR表示部: 下顎 左
        pd_pcr48 = LowerTeethFramePDPCRView(self, fdi_no="48")
        pd_pcr48.grid(row=10, column=0)

        pd_pcr47 = LowerTeethFramePDPCRView(self, fdi_no="47")
        pd_pcr47.grid(row=10, column=1)

        pd_pcr46 = LowerTeethFramePDPCRView(self, fdi_no="46")
        pd_pcr46.grid(row=10, column=2)

        pd_pcr45 = LowerTeethFramePDPCRView(self, fdi_no="45")
        pd_pcr45.grid(row=10, column=3)

        pd_pcr44 = LowerTeethFramePDPCRView(self, fdi_no="44")
        pd_pcr44.grid(row=10, column=4)

        pd_pcr43 = LowerTeethFramePDPCRView(self, fdi_no="43")
        pd_pcr43.grid(row=10, column=5)

        pd_pcr42 = LowerTeethFramePDPCRView(self, fdi_no="42")
        pd_pcr42.grid(row=10, column=6)

        pd_pcr41 = LowerTeethFramePDPCRView(self, fdi_no="41")
        pd_pcr41.grid(row=10, column=7)

        # 下顎の右側・左側の間に入れるスペーサー
        spacer8 = tkinter.Frame(self)
        spacer8.grid(row=10, column=8, padx=30)

        pd_pcr31 = LowerTeethFramePDPCRView(self, fdi_no="31")
        pd_pcr31.grid(row=10, column=9)

        pd_pcr32 = LowerTeethFramePDPCRView(self, fdi_no="32")
        pd_pcr32.grid(row=10, column=10)

        pd_pcr33 = LowerTeethFramePDPCRView(self, fdi_no="33")
        pd_pcr33.grid(row=10, column=11)

        pd_pcr34 = LowerTeethFramePDPCRView(self, fdi_no="34")
        pd_pcr34.grid(row=10, column=12)

        pd_pcr35 = LowerTeethFramePDPCRView(self, fdi_no="35")
        pd_pcr35.grid(row=10, column=13)

        pd_pcr36 = LowerTeethFramePDPCRView(self, fdi_no="36")
        pd_pcr36.grid(row=10, column=14)

        pd_pcr37 = LowerTeethFramePDPCRView(self, fdi_no="37")
        pd_pcr37.grid(row=10, column=15)

        pd_pcr38 = LowerTeethFramePDPCRView(self, fdi_no="38")
        pd_pcr38.grid(row=10, column=16)


        # PDPCR表示部:下部のサマリー表示部と上下を分けるセパレータ
        spacer9 = tkinter.Frame(self)
        spacer9.grid(row=11, column=0, pady=10)


        # PD4mm以上の歯数の計算結果表示
        # 残存歯のカウント表示用ラベルを作成
        pd_pcr_over_threshold_counter = tkinter.IntVar()
        pd_pcr_over_threshold_label_widget = tkinter.Label(self, text="PD 4mm以上の歯数")
        pd_pcr_over_threshold_label_widget.grid(row=12, column=0, columnspan=2, sticky=tkinter.W)
        pd_pcr_over_threshold_widget = tkinter.Label(self, textvariable=remaining_teeth_counter)
        pd_pcr_over_threshold_widget.grid(row=12, column=2, sticky=tkinter.W)
        pd_pcr_over_threshold_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        pd_pcr_painted_counter = tkinter.IntVar()
        pd_pcr_painted_label_widget = tkinter.Label(self, text="プラーク歯面数")
        pd_pcr_painted_label_widget.grid(row=13, column=0, columnspan=2, sticky=tkinter.W)
        pd_pcr_painted_widget = tkinter.Label(self, textvariable=painted_counter)
        pd_pcr_painted_widget.grid(row=13, column=2, sticky=tkinter.W)
        pd_pcr_painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        pd_pcr_percentage = tkinter.DoubleVar()
        pd_pcr_percentage_label_widget = tkinter.Label(self, text="agPCR割合")
        pd_pcr_percentage_label_widget.grid(row=14, column=0, columnspan=2, sticky=tkinter.W)
        pd_pcr_percentage_widget = tkinter.Label(self, textvariable=percentage)
        pd_pcr_percentage_widget.grid(row=14, column=2, sticky=tkinter.W)
        pd_pcr_percentage.set(0.000)  # デフォルト値