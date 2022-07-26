import tkinter
from . import UpperTeethFrame
from . import LowerTeethFrame
from .. import TeethCanvas


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
        spacer4.grid(row=3, column=0, pady=30)


        # PDPCRの表示部: 上顎 左
        pd_pcr18 = TeethCanvas(self)
        pd_pcr18.grid(row=4, column=0)

        pd_pcr17 = TeethCanvas(self)
        pd_pcr17.grid(row=4, column=1)

        pd_pcr16 = TeethCanvas(self)
        pd_pcr16.grid(row=4, column=2)

        pd_pcr15 = TeethCanvas(self)
        pd_pcr15.grid(row=4, column=3)

        pd_pcr14 = TeethCanvas(self)
        pd_pcr14.grid(row=4, column=4)

        pd_pcr13 = TeethCanvas(self)
        pd_pcr13.grid(row=4, column=5)

        pd_pcr12 = TeethCanvas(self)
        pd_pcr12.grid(row=4, column=6)

        pd_pcr11 = TeethCanvas(self)
        pd_pcr11.grid(row=4, column=7)


        # PDPCRの表示部: 上顎の右側・左側を分けるスペーサー
        spacer5 = tkinter.Frame(self)
        spacer5.grid(row=4, column=8, padx=30)


        # PDPCR表示部: 上顎 右
        pd_pcr21 = TeethCanvas(self)
        pd_pcr21.grid(row=4, column=9)

        pd_pcr22 = TeethCanvas(self)
        pd_pcr22.grid(row=4, column=10)

        pd_pcr23 = TeethCanvas(self)
        pd_pcr23.grid(row=4, column=11)

        pd_pcr24 = TeethCanvas(self)
        pd_pcr24.grid(row=4, column=12)

        pd_pcr25 = TeethCanvas(self)
        pd_pcr25.grid(row=4, column=13)

        pd_pcr26 = TeethCanvas(self)
        pd_pcr26.grid(row=4, column=14)

        pd_pcr27 = TeethCanvas(self)
        pd_pcr27.grid(row=4, column=15)

        pd_pcr28 = TeethCanvas(self)
        pd_pcr28.grid(row=4, column=16)


        # PDPCR表示部:上下のコンポーネントのスペースを開ける
        spacer6 = tkinter.Frame(self)
        spacer6.grid(row=5, column=0, pady=10)


        # PDPCR表示部: 下顎 左
        pd_pcr48 = TeethCanvas(self)
        pd_pcr48.grid(row=6, column=0)

        pd_pcr47 = TeethCanvas(self)
        pd_pcr47.grid(row=6, column=1)

        pd_pcr46 = TeethCanvas(self)
        pd_pcr46.grid(row=6, column=2)

        pd_pcr45 = TeethCanvas(self)
        pd_pcr45.grid(row=6, column=3)

        pd_pcr44 = TeethCanvas(self)
        pd_pcr44.grid(row=6, column=4)

        pd_pcr43 = TeethCanvas(self)
        pd_pcr43.grid(row=6, column=5)

        pd_pcr42 = TeethCanvas(self)
        pd_pcr42.grid(row=6, column=6)

        pd_pcr41 = TeethCanvas(self)
        pd_pcr41.grid(row=6, column=7)

        # 下顎の右側・左側の間に入れるスペーサー
        spacer7 = tkinter.Frame(self)
        spacer7.grid(row=6, column=8, padx=30)

        pd_pcr31 = TeethCanvas(self)
        pd_pcr31.grid(row=6, column=9)

        pd_pcr32 = TeethCanvas(self)
        pd_pcr32.grid(row=6, column=10)

        pd_pcr33 = TeethCanvas(self)
        pd_pcr33.grid(row=6, column=11)

        pd_pcr34 = TeethCanvas(self)
        pd_pcr34.grid(row=6, column=12)

        pd_pcr35 = TeethCanvas(self)
        pd_pcr35.grid(row=6, column=13)

        pd_pcr36 = TeethCanvas(self)
        pd_pcr36.grid(row=6, column=14)

        pd_pcr37 = TeethCanvas(self)
        pd_pcr37.grid(row=6, column=15)

        pd_pcr38 = TeethCanvas(self)
        pd_pcr38.grid(row=6, column=16)


        # PDPCR表示部:上下のコンポーネントのスペースを開ける
        spacer7 = tkinter.Frame(self)
        spacer7.grid(row=7, column=0, pady=20)


        # 残存歯の計算結果表示
        # 残存歯のカウント表示用ラベルを作成
        remaining_teeth_counter = tkinter.IntVar()
        remaining_teeth_label_widget = tkinter.Label(self, text="残存歯")
        remaining_teeth_label_widget.grid(row=8, column=0, sticky=tkinter.E)
        remaining_teeth_widget = tkinter.Label(self, textvariable=remaining_teeth_counter)
        remaining_teeth_widget.grid(row=8, column=1, sticky=tkinter.W)
        remaining_teeth_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        painted_counter = tkinter.IntVar()
        painted_label_widget = tkinter.Label(self, text="プラーク面数")
        painted_label_widget.grid(row=9, column=0, sticky=tkinter.E)
        painted_widget = tkinter.Label(self, textvariable=painted_counter)
        painted_widget.grid(row=9, column=1, sticky=tkinter.W)
        painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        percentage = tkinter.DoubleVar()
        percentage_label_widget = tkinter.Label(self, text="割合")
        percentage_label_widget.grid(row=10, column=0, sticky=tkinter.E)
        percentage_widget = tkinter.Label(self, textvariable=percentage)
        percentage_widget.grid(row=10, column=1, sticky=tkinter.W)
        percentage.set(0.000)  # デフォルト値
