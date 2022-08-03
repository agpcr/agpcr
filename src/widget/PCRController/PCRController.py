import tkinter
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
        super().__init__(master, pady=0)

        # 歯の欠損状態が変化した際のコールバック関数
        self.on_change_missing_callback = on_change_missing_callback

        # PDの状態が変化した際のコールバック関数
        self.on_change_probing_depth_callback = on_change_probing_depth_callback

        # 歯面の状態が変化した際のコールバック関数
        self.on_change_teeth_plane_callback = on_change_teeth_plane_callback

        margin = 5

        # PCR入力部: 上顎 左の入力UI
        self.t18 = UpperTeethFrame(self,
                                   fdi_number=18,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t18.grid(row=0, column=0, padx=margin)

        self.t17 = UpperTeethFrame(self,
                                   fdi_number=17,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t17.grid(row=0, column=1, padx=margin)

        self.t16 = UpperTeethFrame(self,
                                   fdi_number=16,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t16.grid(row=0, column=2, padx=margin)

        self.t15 = UpperTeethFrame(self,
                                   fdi_number=15,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t15.grid(row=0, column=3, padx=margin)

        self.t14 = UpperTeethFrame(self,
                                   fdi_number=14,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t14.grid(row=0, column=4, padx=margin)

        self.t13 = UpperTeethFrame(self,
                                   fdi_number=13,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t13.grid(row=0, column=5, padx=margin)

        self.t12 = UpperTeethFrame(self,
                                   fdi_number=12,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t12.grid(row=0, column=6, padx=margin)

        self.t11 = UpperTeethFrame(self,
                                   fdi_number=11,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t11.grid(row=0, column=7, padx=margin)


        # PCR入力部: 上顎の右側・左側の間に入るスペーサー
        spacer1 = tkinter.Frame(self)
        spacer1.grid(row=0, column=8, padx=30)


        # PCR入力部: 上顎 右の入力UI
        self.t21 = UpperTeethFrame(self,
                                   fdi_number=21,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t21.grid(row=0, column=9, padx=margin)

        self.t22 = UpperTeethFrame(self,
                                   fdi_number=22,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t22.grid(row=0, column=10, padx=margin)

        self.t23 = UpperTeethFrame(self,
                                   fdi_number=23,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t23.grid(row=0, column=11, padx=margin)

        self.t24 = UpperTeethFrame(self,
                                   fdi_number=24,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t24.grid(row=0, column=12, padx=margin)

        self.t25 = UpperTeethFrame(self,
                                   fdi_number=25,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t25.grid(row=0, column=13, padx=margin)

        self.t26 = UpperTeethFrame(self,
                                   fdi_number=26,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t26.grid(row=0, column=14, padx=margin)

        self.t27 = UpperTeethFrame(self,
                                   fdi_number=27,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t27.grid(row=0, column=15, padx=margin)

        self.t28 = UpperTeethFrame(self,
                                   fdi_number=28,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t28.grid(row=0, column=16, padx=margin)



        # PCR入力部: 上下のコンポーネントのスペースを開ける
        spacer2 = tkinter.Frame(self)
        spacer2.grid(row=1, column=0, pady=10)



        # PCR入力部: 下顎 左の入力UI
        self.t48 = LowerTeethFrame(self,
                                   fdi_number=48,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t48.grid(row=2, column=0, padx=margin)

        self.t47 = LowerTeethFrame(self,
                                   fdi_number=47,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t47.grid(row=2, column=1, padx=margin)

        self.t46 = LowerTeethFrame(self,
                                   fdi_number=46,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t46.grid(row=2, column=2, padx=margin)

        self.t45 = LowerTeethFrame(self,
                                   fdi_number=45,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t45.grid(row=2, column=3, padx=margin)

        self.t44 = LowerTeethFrame(self,
                                   fdi_number=44,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t44.grid(row=2, column=4, padx=margin)

        self.t43 = LowerTeethFrame(self,
                                   fdi_number=43,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t43.grid(row=2, column=5, padx=margin)

        self.t42 = LowerTeethFrame(self,
                                   fdi_number=42,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t42.grid(row=2, column=6, padx=margin)

        self.t41 = LowerTeethFrame(self,
                                   fdi_number=41,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t41.grid(row=2, column=7, padx=margin)


        # PCR入力部: 下顎の右側・左側の間に入れるスペーサー
        spacer3 = tkinter.Frame(self)
        spacer3.grid(row=2, column=8, padx=30)


        # PCR入力部: 下顎 右の入力UI
        self.t31 = LowerTeethFrame(self,
                                   fdi_number=31,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t31.grid(row=2, column=9, padx=margin)

        self.t32 = LowerTeethFrame(self,
                                   fdi_number=32,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t32.grid(row=2, column=10, padx=margin)

        self.t33 = LowerTeethFrame(self,
                                   fdi_number=33,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t33.grid(row=2, column=11, padx=margin)

        self.t34 = LowerTeethFrame(self,
                                   fdi_number=34,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t34.grid(row=2, column=12, padx=margin)

        self.t35 = LowerTeethFrame(self,
                                   fdi_number=35,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t35.grid(row=2, column=13, padx=margin)

        self.t36 = LowerTeethFrame(self,
                                   fdi_number=36,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t36.grid(row=2, column=14, padx=margin)

        self.t37 = LowerTeethFrame(self,
                                   fdi_number=37,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t37.grid(row=2, column=15, padx=margin)

        self.t38 = LowerTeethFrame(self,
                                   fdi_number=38,
                                   on_change_missing_callback=self.on_change_missing,
                                   on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                   on_change_teeth_plane_callback=self.on_change_teeth_plane)
        self.t38.grid(row=2, column=16, padx=margin)

        self.pcr_frames = {
            18: self.t18,
            17: self.t17,
            16: self.t16,
            15: self.t15,
            14: self.t14,
            13: self.t13,
            12: self.t12,
            11: self.t11,

            21: self.t21,
            22: self.t22,
            23: self.t23,
            24: self.t24,
            25: self.t25,
            26: self.t26,
            27: self.t27,
            28: self.t28,

            48: self.t48,
            47: self.t47,
            46: self.t46,
            45: self.t45,
            44: self.t44,
            43: self.t43,
            42: self.t42,
            41: self.t41,

            31: self.t31,
            32: self.t32,
            33: self.t33,
            34: self.t34,
            35: self.t35,
            36: self.t36,
            37: self.t37,
            38: self.t38,
        }

        #####################################################
        # PCR入力部と、PDPCRの表示部を上下に分けるスペーサー
        #####################################################
        spacer4 = tkinter.Frame(self)
        spacer4.grid(row=3, column=0, pady=10)

        # 残存歯の計算結果表示
        # 残存歯のカウント表示用ラベルを作成
        self.remaining_teeth_counter = tkinter.IntVar()
        remaining_teeth_label_widget = tkinter.Label(self, text="残存歯")
        remaining_teeth_label_widget.grid(row=4, column=0, columnspan=2, sticky=tkinter.W)
        remaining_teeth_widget = tkinter.Label(self, textvariable=self.remaining_teeth_counter)
        remaining_teeth_widget.grid(row=4, column=2, sticky=tkinter.W)
        self.remaining_teeth_counter.set(0)  # デフォルト値

        # プラーク面数結果表示
        # 歯面の塗られた数をカウント
        self.painted_counter = tkinter.IntVar()
        painted_label_widget = tkinter.Label(self, text="プラーク歯面数")
        painted_label_widget.grid(row=5, column=0, columnspan=2, sticky=tkinter.W)
        painted_widget = tkinter.Label(self, textvariable=self.painted_counter)
        painted_widget.grid(row=5, column=2, sticky=tkinter.W)
        self.painted_counter.set(0)  # デフォルト値

        # 割合結果表示
        # 割合を表示
        self.percentage = tkinter.StringVar()
        percentage_label_widget = tkinter.Label(self, text="割合")
        percentage_label_widget.grid(row=6, column=0, columnspan=2, sticky=tkinter.W)
        percentage_widget = tkinter.Label(self, textvariable=self.percentage)
        percentage_widget.grid(row=6, column=2, sticky=tkinter.W)
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