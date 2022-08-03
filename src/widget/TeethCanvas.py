import tkinter
from enum import Enum


class TeethPlane(Enum):
    TOP = 'TOP'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    BOTTOM = 'BOTTOM'


class TeethState(Enum):
    NORMAL = 'NORMAL'
    MISSING = 'MISSING'


class TeethPlaneState(Enum):
    NORMAL = 'NORMAL'
    PLAQUE = 'PLAQUE'
    UNDER_PD = 'UNDER_PD'


class TeethCanvas(tkinter.Frame):
    def __init__(self,
                 master=None,
                 normal_color='white',
                 plaque_color='red',
                 missing_color='gray54',
                 under_pd_threshold_color='gray26',
                 is_paintable=True,
                 on_change_teeth_plane_callback=None,
                 initial_teeth_state=TeethState.NORMAL):
        super().__init__(master)

        # １歯全体の状態
        self.teeth_state = initial_teeth_state

        # 歯面の状態
        self.teeth_plane_state = {
            TeethPlane.TOP: TeethPlaneState.NORMAL,
            TeethPlane.RIGHT: TeethPlaneState.NORMAL,
            TeethPlane.BOTTOM: TeethPlaneState.NORMAL,
            TeethPlane.LEFT: TeethPlaneState.NORMAL,
        }

        self.on_change_teeth_plane_callback = on_change_teeth_plane_callback

        self.normal_color = normal_color  # 標準状態の歯面を表現する色
        self.plaque_color = plaque_color  # 歯垢付着面を表現する色
        self.missing_color = missing_color  # 欠損歯を表現する色
        self.under_pd_threshold_color = under_pd_threshold_color  # PD警告がない状態を表す色

        self.is_paintable = is_paintable  # Trueであれば歯面のクリックで色を変更できる

        pcr_teeth_canvas_width = 50
        pcr_teeth_canvas_height = 50

        self.canvas = tkinter.Canvas(self,
                                     width=pcr_teeth_canvas_width,
                                     height=pcr_teeth_canvas_height,
                                     bg='light yellow')
        self.canvas.pack()

        canvas_width = pcr_teeth_canvas_width + 2
        canvas_height = pcr_teeth_canvas_height + 2

        # 初期表示の歯面の色を状態に応じて決定する
        default_plane_color = self.normal_color
        if self.teeth_state is TeethState.MISSING:
            default_plane_color = self.missing_color

        self.ue = self.canvas.create_polygon(4, 4,
                                             canvas_width, 4,
                                             (canvas_width+4) / 2, (canvas_height+4) / 2,
                                             fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                             tags=str(id) + "_l")

        self.migi = self.canvas.create_polygon(canvas_width, 4,
                                               canvas_width, canvas_height,
                                               (canvas_width+4) / 2, (canvas_height+4) / 2,
                                               fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                               tags=str(id) + "_l")

        self.shita = self.canvas.create_polygon(canvas_width, canvas_height,
                                                4, canvas_height,
                                                (canvas_width+4) / 2, (canvas_height+4) / 2,
                                                fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                                tags=str(id) + "_l")

        self.hidari = self.canvas.create_polygon(4, canvas_height,
                                                 4, 4,
                                                 (canvas_width+4) / 2, (canvas_height+4) / 2,
                                                 fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                                 tags=str(id) + "_l")

        # obj_idとTeethPlaneの対応表
        self.obj_id_to_teeth_plane = {
            self.ue: TeethPlane.TOP,
            self.migi: TeethPlane.RIGHT,
            self.hidari: TeethPlane.LEFT,
            self.shita: TeethPlane.BOTTOM
        }

        # TeethPlaneとobj_idの対応表
        self.teeth_plane_to_obj_id = {
            TeethPlane.TOP: self.ue,
            TeethPlane.RIGHT: self.migi,
            TeethPlane.LEFT: self.hidari,
            TeethPlane.BOTTOM: self.shita
        }

        if self.is_paintable:
            self.canvas.tag_bind(self.ue, "<Button-1>", lambda ev, obj_id=self.ue: self.toggle_plane(ev, obj_id))
            self.canvas.tag_bind(self.migi, "<Button-1>", lambda ev, obj_id=self.migi: self.toggle_plane(ev, obj_id))
            self.canvas.tag_bind(self.shita, "<Button-1>", lambda ev, obj_id=self.shita: self.toggle_plane(ev, obj_id))
            self.canvas.tag_bind(self.hidari, "<Button-1>",
                                 lambda ev, obj_id=self.hidari: self.toggle_plane(ev, obj_id))

    def toggle_missing(self, is_missing):
        if is_missing:
            # 全歯面を欠損歯色に塗る
            for obj_id in self.teeth_plane_to_obj_id.values():
                self.canvas.itemconfigure(obj_id, fill=self.missing_color)

            # 欠損歯に設定する
            self.teeth_state = TeethState.MISSING
        else:
            # 全歯面を現在の状態に応じて塗り戻す
            for plane, state in self.teeth_plane_state.items():
                if state == TeethPlaneState.NORMAL:
                    self.canvas.itemconfigure(self.teeth_plane_to_obj_id[plane], fill=self.normal_color)
                if state == TeethPlaneState.PLAQUE:
                    self.canvas.itemconfigure(self.teeth_plane_to_obj_id[plane], fill=self.plaque_color)
                if state == TeethPlaneState.UNDER_PD:
                    self.canvas.itemconfigure(self.teeth_plane_to_obj_id[plane], fill=self.under_pd_threshold_color)
            # 健康歯に設定する
            self.teeth_state = TeethState.NORMAL

    def toggle_plane(self, ev, obj_id):
        # 欠損歯状態でなければ面の 赤 or 白 トグルを行う
        if self.teeth_state is not TeethState.MISSING:
            teeth_plane = self.obj_id_to_teeth_plane[obj_id]
            now_plane_state = self.teeth_plane_state[teeth_plane]

            if now_plane_state == TeethPlaneState.NORMAL:
                next_color = self.plaque_color
                next_state = TeethPlaneState.PLAQUE
            else:
                next_color = self.normal_color
                next_state = TeethPlaneState.NORMAL

            # 歯面の色を変更する
            self.canvas.itemconfigure(obj_id, fill=next_color)

            # 歯面の状態を変更する
            self.teeth_plane_state[teeth_plane] = next_state

            if self.on_change_teeth_plane_callback is not None:
                self.on_change_teeth_plane_callback(self.obj_id_to_teeth_plane[obj_id],
                                                    next_color,
                                                    self.get_teeth_plane_state())

    def get_teeth_plane_state(self):
        return self.teeth_plane_state

    def set_teeth_plane_state(self, teeth_plane, teeth_plane_state):
        obj_id = self.teeth_plane_to_obj_id[teeth_plane]

        color = 'white'
        if teeth_plane_state is TeethPlaneState.UNDER_PD:
            color = self.under_pd_threshold_color
            self.teeth_plane_state[teeth_plane] = TeethPlaneState.UNDER_PD
        if teeth_plane_state == TeethPlaneState.PLAQUE:
            color = self.plaque_color
            self.teeth_plane_state[teeth_plane] = TeethPlaneState.PLAQUE
        if teeth_plane_state == TeethPlaneState.NORMAL:
            color = self.normal_color
            self.teeth_plane_state[teeth_plane] = TeethPlaneState.NORMAL

        # 歯面の色を変更する
        self.canvas.itemconfigure(obj_id, fill=color)

        if self.on_change_teeth_plane_callback is not None:
            self.on_change_teeth_plane_callback(teeth_plane, color, self.get_teeth_plane_state())

    def get_teeth_state(self):
        return self.teeth_state
