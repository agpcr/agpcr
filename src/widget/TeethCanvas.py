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
                 is_missing=False,
                 is_under_pd=False):
        super().__init__(master)
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

        # 欠損歯状態の場合はTrue
        self.is_missing = False

        # PDに異常がない場合はTrue
        self.is_under_pd = True

        self.canvas = tkinter.Canvas(self,
                                     width=pcr_teeth_canvas_width,
                                     height=pcr_teeth_canvas_height,
                                     bg='light yellow')
        self.canvas.pack()

        canvas_width = pcr_teeth_canvas_width + 2
        canvas_height = pcr_teeth_canvas_height + 2

        # 初期表示の歯面の色を状態に応じて決定する
        default_plane_color = 'white'
        if is_missing:
            default_plane_color = self.missing_color

        if is_under_pd:
            default_plane_color = self.under_pd_threshold_color

        self.ue = self.canvas.create_polygon(2, 2,
                                             canvas_width, 2,
                                             canvas_width / 2, canvas_height / 2,
                                             fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                             tags=str(id) + "_l")

        self.migi = self.canvas.create_polygon(canvas_width, 2,
                                               canvas_width, canvas_height,
                                               canvas_width / 2, canvas_height / 2,
                                               fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                               tags=str(id) + "_l")

        self.shita = self.canvas.create_polygon(canvas_width, canvas_height,
                                                2, canvas_height,
                                                canvas_width / 2, canvas_height / 2,
                                                fill=default_plane_color, outline='black', width=2.0, joinstyle=tkinter.BEVEL,
                                                tags=str(id) + "_l")

        self.hidari = self.canvas.create_polygon(2, canvas_height,
                                                 2, 2,
                                                 canvas_width / 2, canvas_height / 2,
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
        self.is_missing = is_missing

        if self.is_missing:
            self.canvas.itemconfigure(self.ue, fill=self.missing_color)
            self.canvas.itemconfigure(self.migi, fill=self.missing_color)
            self.canvas.itemconfigure(self.shita, fill=self.missing_color)
            self.canvas.itemconfigure(self.hidari, fill=self.missing_color)
        else:
            if (self.is_under_pd is True) and (self.is_paintable is False):
                self.canvas.itemconfigure(self.ue, fill=self.under_pd_threshold_color)
                self.canvas.itemconfigure(self.migi, fill=self.under_pd_threshold_color)
                self.canvas.itemconfigure(self.shita, fill=self.under_pd_threshold_color)
                self.canvas.itemconfigure(self.hidari, fill=self.under_pd_threshold_color)
            else:
                self.canvas.itemconfigure(self.ue, fill='white')
                self.canvas.itemconfigure(self.migi, fill='white')
                self.canvas.itemconfigure(self.shita, fill='white')
                self.canvas.itemconfigure(self.hidari, fill='white')

    def set_under_pd(self, is_under_pd, teeth_plane):
        self.is_under_pd = is_under_pd

        obj_id = self.teeth_plane_to_obj_id[teeth_plane]
        if self.is_under_pd:
            self.canvas.itemconfigure(obj_id, fill=self.under_pd_threshold_color)
        else:
            self.canvas.itemconfigure(obj_id, fill='white')


    def toggle_plane(self, ev, obj_id):
        # 欠損歯状態でなければ面の 赤 or 白 トグルを行う
        if not self.is_missing:
            now_color = self.canvas.itemcget(obj_id, 'fill')
            next_color, cnt = (self.plaque_color, 1) if now_color == 'white' else ('white', -1)

            self.canvas.itemconfigure(obj_id, fill=next_color)
            if self.on_change_teeth_plane_callback is not None:
                self.on_change_teeth_plane_callback(self.obj_id_to_teeth_plane[obj_id],
                                                    next_color,
                                                    self.get_teeth_plane_state())

    def get_teeth_plane_state(self):
        return self.teeth_plane_state

    def paint_plane(self, color, position):
        # 外部から指定されたpositionと対応する歯面を指定のcolorで塗る
        obj_id = self.teeth_plane_to_obj_id[position]
        self.canvas.itemconfigure(obj_id, fill=color)
        if self.on_change_teeth_plane_callback is not None:
            self.on_change_teeth_plane_callback(position, color, self.get_teeth_plane_state())

    def has_plaque(self, position):
        obj_id = self.teeth_plane_to_obj_id[position]
        now_color = self.canvas.itemcget(obj_id, 'fill')
        return now_color == self.plaque_color

    def set_teeth_plane_state(self, teeth_plane, teeth_plane_state):
        obj_id = self.teeth_plane_to_obj_id[teeth_plane]

        color = 'white'
        if teeth_plane_state == TeethPlaneState.PLAQUE:
            color = self.plaque_color
            self.teeth_plane_state[teeth_plane] = TeethPlaneState.PLAQUE
        if teeth_plane_state == TeethPlaneState.NORMAL:
            color = self.normal_color
            self.teeth_plane_state[teeth_plane] = TeethPlaneState.NORMAL
        if teeth_plane_state == TeethPlaneState.UNDER_PD:
            color = self.under_pd_threshold_color
            self.teeth_plane_state[teeth_plane] = TeethPlaneState.UNDER_PD

        # 歯面の色を変更する
        self.canvas.itemconfigure(obj_id, fill=color)

        if self.on_change_teeth_plane_callback is not None:
            self.on_change_teeth_plane_callback(teeth_plane, color, self.get_teeth_plane_state())