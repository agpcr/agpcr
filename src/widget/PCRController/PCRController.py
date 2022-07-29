import tkinter
from . import UpperTeethFrame
from . import LowerTeethFrame


class PCRController(tkinter.Frame):
    def __init__(self, master=None, is_missing_callback=None, on_change_probing_depth_callback=None):
        super().__init__(master, pady=0)

        margin = 5

        # PCR入力部: 上顎 左の入力UI
        t18 = UpperTeethFrame(self,
                              fdi_number=18,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t18.grid(row=0, column=0, padx=margin)

        t17 = UpperTeethFrame(self,
                              fdi_number=17,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t17.grid(row=0, column=1, padx=margin)

        t16 = UpperTeethFrame(self,
                              fdi_number=16,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t16.grid(row=0, column=2, padx=margin)

        t15 = UpperTeethFrame(self,
                              fdi_number=15,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t15.grid(row=0, column=3, padx=margin)

        t14 = UpperTeethFrame(self,
                              fdi_number=14,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t14.grid(row=0, column=4, padx=margin)

        t13 = UpperTeethFrame(self,
                              fdi_number=13,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t13.grid(row=0, column=5, padx=margin)

        t12 = UpperTeethFrame(self,
                              fdi_number=12,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t12.grid(row=0, column=6, padx=margin)

        t11 = UpperTeethFrame(self,
                              fdi_number=11,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t11.grid(row=0, column=7, padx=margin)


        # PCR入力部: 上顎の右側・左側の間に入るスペーサー
        spacer1 = tkinter.Frame(self)
        spacer1.grid(row=0, column=8, padx=30)


        # PCR入力部: 上顎 右の入力UI
        t21 = UpperTeethFrame(self,
                              fdi_number=21,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t21.grid(row=0, column=9, padx=margin)

        t22 = UpperTeethFrame(self,
                              fdi_number=22,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t22.grid(row=0, column=10, padx=margin)

        t23 = UpperTeethFrame(self,
                              fdi_number=23,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t23.grid(row=0, column=11, padx=margin)

        t24 = UpperTeethFrame(self,
                              fdi_number=24,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t24.grid(row=0, column=12, padx=margin)

        t25 = UpperTeethFrame(self,
                              fdi_number=25,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t25.grid(row=0, column=13, padx=margin)

        t26 = UpperTeethFrame(self,
                              fdi_number=26,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t26.grid(row=0, column=14, padx=margin)

        t27 = UpperTeethFrame(self,
                              fdi_number=27,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t27.grid(row=0, column=15, padx=margin)

        t28 = UpperTeethFrame(self,
                              fdi_number=28,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t28.grid(row=0, column=16, padx=margin)



        # PCR入力部: 上下のコンポーネントのスペースを開ける
        spacer2 = tkinter.Frame(self)
        spacer2.grid(row=1, column=0, pady=10)



        # PCR入力部: 下顎 左の入力UI
        t48 = LowerTeethFrame(self,
                              fdi_number=48,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t48.grid(row=2, column=0, padx=margin)

        t47 = LowerTeethFrame(self,
                              fdi_number=47,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t47.grid(row=2, column=1, padx=margin)

        t46 = LowerTeethFrame(self,
                              fdi_number=46,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t46.grid(row=2, column=2, padx=margin)

        t45 = LowerTeethFrame(self,
                              fdi_number=45,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t45.grid(row=2, column=3, padx=margin)

        t44 = LowerTeethFrame(self,
                              fdi_number=44,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t44.grid(row=2, column=4, padx=margin)

        t43 = LowerTeethFrame(self,
                              fdi_number=43,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t43.grid(row=2, column=5, padx=margin)

        t42 = LowerTeethFrame(self,
                              fdi_number=42,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t42.grid(row=2, column=6, padx=margin)

        t41 = LowerTeethFrame(self,
                              fdi_number=41,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t41.grid(row=2, column=7, padx=margin)


        # PCR入力部: 下顎の右側・左側の間に入れるスペーサー
        spacer3 = tkinter.Frame(self)
        spacer3.grid(row=2, column=8, padx=30)


        # PCR入力部: 下顎 右の入力UI
        t31 = LowerTeethFrame(self,
                              fdi_number=31,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t31.grid(row=2, column=9, padx=margin)

        t32 = LowerTeethFrame(self,
                              fdi_number=32,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t32.grid(row=2, column=10, padx=margin)

        t33 = LowerTeethFrame(self,
                              fdi_number=33,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t33.grid(row=2, column=11, padx=margin)

        t34 = LowerTeethFrame(self,
                              fdi_number=34,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t34.grid(row=2, column=12, padx=margin)

        t35 = LowerTeethFrame(self,
                              fdi_number=35,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t35.grid(row=2, column=13, padx=margin)

        t36 = LowerTeethFrame(self,
                              fdi_number=36,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t36.grid(row=2, column=14, padx=margin)

        t37 = LowerTeethFrame(self,
                              fdi_number=37,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
        t37.grid(row=2, column=15, padx=margin)

        t38 = LowerTeethFrame(self,
                              fdi_number=38,
                              is_missing_callback=is_missing_callback,
                              on_change_pd=on_change_probing_depth_callback)
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
