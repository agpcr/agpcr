# -*- coding: UTF-8 -*-
import tkinter
import enum


def create_initial_data(tooth_num, text, jaw, side):
    return {
        'tooth_num': tooth_num,
        'button_label': str(text),
        'jaw': jaw,
        'side': side,
        'available': True
    }


# 残存歯のボタンのON・OFF
def remaining_toggle(event, tooth_num):
    event.widget['fg'] = 'red' if (event.widget['fg'] == 'black') else 'black'  # 赤→黒 と 黒→赤 の色反転
    target = [d for d in teeth if d.get('tooth_num') == tooth_num][0]
    target['available'] = not (target['available'])  # 現在値を反転（有効→無効、無効→有効）

    if target['available']:
        # 残存歯に戻された為、その歯牙の全ての面を白にする
        canvas.itemconfigure(str(tooth_num) + "_m", fill='white')
        canvas.itemconfigure(str(tooth_num) + "_d", fill='white')
        canvas.itemconfigure(str(tooth_num) + "_b", fill='white')
        canvas.itemconfigure(str(tooth_num) + "_l", fill='white')
    else:
        # 既に赤く塗られてる面があった場合、その数をカウンタから減算する
        tags = [str(tooth_num) + "_m", str(tooth_num) + "_d", str(tooth_num) + "_b", str(tooth_num) + "_l"]
        painted_tags = [tag for tag in tags if canvas.itemcget(tag, 'fill') == 'red']
        painted_counter.set(painted_counter.get() - len(painted_tags))

        # 欠損歯とされた為、その歯牙全ての面をグレーにする
        canvas.itemconfigure(str(tooth_num) + "_m", fill='gray')
        canvas.itemconfigure(str(tooth_num) + "_d", fill='gray')
        canvas.itemconfigure(str(tooth_num) + "_b", fill='gray')
        canvas.itemconfigure(str(tooth_num) + "_l", fill='gray')

    remaining_teeth_counter.set(sum([1 for tooth in teeth if tooth.get("available")]))
    update_percentage()


# 歯面の赤・白を切り替える
def toggle_canvas_item_color(event, tooth_num):
    target = [d for d in teeth if d.get('tooth_num') == tooth_num][0]

    if target['available']:
        next_color, cnt = ('red', 1) if canvas.itemcget('current', 'fill') == 'white' else ('white', -1)
        canvas.itemconfigure('current', fill=next_color)
        painted_counter.set(painted_counter.get() + cnt)

    update_percentage()


# 割合を更新する
def update_percentage():
    percent = (painted_counter.get() / (remaining_teeth_counter.get() * 4)) * 100
    percentage.set(round(percent, 3))


# 残存歯のコントロールボタンを作成する
def create_button(root, text, tooth_num, side):
    button = tkinter.Button(root, text=text, fg='black', width='3')
    button.bind("<Button-1>", lambda ev, tooth_num=tooth_num: remaining_toggle(ev, tooth_num))
    if tooth_num <= 28:
        button.pack(side=tkinter.LEFT)
    else:
        button.pack(side=tkinter.RIGHT)


# 正中と歯牙の番号とサイズと部位情報(顎・側)情報からXYの値を返す関数
def calc_shimen_xy(center_x, tooth_num, size, jaw, side):
    if (jaw is Jaw.Upper) and (side is Side.Right):
        y, x = 30, center_x - (size * (tooth_num - 10))
        return x, y
    elif (jaw is Jaw.Lower) and (side is Side.Right):
        y, x = 70, center_x - (size * (tooth_num - 40))
        return x, y

    elif (jaw is Jaw.Upper) and (side is Side.Left):
        y, x = 30, center_x + (size * (tooth_num - 20))
        return x, y
    elif (jaw is Jaw.Lower) and (side is Side.Left):
        y, x = 70, center_x + (size * (tooth_num - 30))
        return x, y


def create_shimen(canvas, center_x, id, bui_col, jaw, side):
    ll = 30
    x, y = calc_shimen_xy(center_x, id, ll, jaw, side)  # 正中の基点と、1歯を表す正方形1辺の長さ、歯牙の情報からxとyを割り出す

    medial_id = canvas.create_polygon(x, y,
                                      x - (ll / 2), y - (ll / 2),
                                      x + (ll / 2), y - (ll / 2),
                                      fill=bui_col, outline='black', width=2.0, tags=str(id) + "_m")

    distal_id = canvas.create_polygon(x, y,
                                      x + (ll / 2), y + (ll / 2),
                                      x + (ll / 2), y - (ll / 2),
                                      fill=bui_col, outline='black', width=2.0, tags=str(id) + "_d")

    buccal_id = canvas.create_polygon(x, y,
                                      x + (ll / 2), y - (-ll / 2),
                                      x + (-ll / 2), y - (-ll / 2),
                                      fill=bui_col, outline='black', width=2.0, tags=str(id) + "_b")

    lingual_id = canvas.create_polygon(x, y,
                                       x + (-ll / 2), y - (ll / 2),
                                       x + (-ll / 2), y + (ll / 2),
                                       fill=bui_col, outline='black', width=2.0, tags=str(id) + "_l")

    canvas.tag_bind(medial_id, "<Button-1>", lambda ev, tooth_num=id: toggle_canvas_item_color(ev, tooth_num))
    canvas.tag_bind(distal_id, "<Button-1>", lambda ev, tooth_num=id: toggle_canvas_item_color(ev, tooth_num))
    canvas.tag_bind(buccal_id, "<Button-1>", lambda ev, tooth_num=id: toggle_canvas_item_color(ev, tooth_num))
    canvas.tag_bind(lingual_id, "<Button-1>", lambda ev, tooth_num=id: toggle_canvas_item_color(ev, tooth_num))


# ---------

Jaw = enum.Enum('Jaw', 'Upper Lower')
Side = enum.Enum('Side', 'Left Right')

root = tkinter.Tk()
root.title('check sheet')


# 歯のデータを生成
teeth = [create_initial_data(v, v, Jaw.Upper, Side.Right) for v in list(reversed(range(11, 19)))] \
        + [create_initial_data(v, v, Jaw.Upper, Side.Left) for v in range(21, 29)] \
        + [create_initial_data(v, v, Jaw.Lower, Side.Left) for v in list(reversed(range(31, 39)))] \
        + [create_initial_data(v, v, Jaw.Lower, Side.Right) for v in range(41, 49)]


# 残存歯・プラーク面数・割合 等を表示する入れ物を作成
summary_frame = tkinter.Frame(root)

# 残存歯のカウント表示用ラベルを作成
remaining_teeth_counter = tkinter.IntVar()
remaining_teeth_label_widget = tkinter.Label(summary_frame, text="残存歯:")
remaining_teeth_label_widget.grid(row=0, column=0, sticky=tkinter.E)
remaining_teeth_widget = tkinter.Label(summary_frame, textvariable=remaining_teeth_counter)
remaining_teeth_widget.grid(row=0, column=1, sticky=tkinter.W)
remaining_teeth_counter.set(sum([1 for tooth in teeth if tooth.get("available")]))  # デフォルト値

# 歯面の塗られた数をカウント
painted_counter = tkinter.IntVar()
painted_label_widget = tkinter.Label(summary_frame, text="プラーク面数:")
painted_label_widget.grid(row=1, column=0, sticky=tkinter.E)
painted_widget = tkinter.Label(summary_frame, textvariable=painted_counter)
painted_widget.grid(row=1, column=1, sticky=tkinter.W)
painted_counter.set(0)  # デフォルト値

# 割合を表示
percentage = tkinter.DoubleVar()
percentage_label_widget = tkinter.Label(summary_frame, text="割合:")
percentage_label_widget.grid(row=2, column=0, sticky=tkinter.E)
percentage_widget = tkinter.Label(summary_frame, textvariable=percentage)
percentage_widget.grid(row=2, column=1, sticky=tkinter.W)
percentage.set(0.000)  # デフォルト値
summary_frame.pack(anchor=tkinter.W)

upper_buttons_frame = tkinter.Frame(root)
upper_buttons_frame.pack()

canvas_frame = tkinter.Frame(root)
# Canvasの生成
canvas = tkinter.Canvas(canvas_frame, width=514, height=100, bg='light yellow')
canvas.pack()
canvas_frame.pack()

lower_buttons_frame = tkinter.Frame(root)
lower_buttons_frame.pack()

center = 260  # 正中線を400pxの点とする

# 歯のデータからボタンと歯面を作成する
for tooth in teeth:
    if tooth.get('tooth_num') <= 28:
        button_frame = upper_buttons_frame
    else:
        button_frame = lower_buttons_frame

    create_button(button_frame, tooth.get('button_label'), tooth.get('tooth_num'), tooth.get('side'))
    create_shimen(canvas, center, tooth.get('tooth_num'), 'white', tooth.get('jaw'), tooth.get('side'))

root.mainloop()
