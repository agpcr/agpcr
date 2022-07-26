import tkinter


class TeethCanvas(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        pcr_teeth_canvas_width = 50
        pcr_teeth_canvas_height = 50

        canvas = tkinter.Canvas(self, width=pcr_teeth_canvas_width, height=pcr_teeth_canvas_height, bg='light yellow')
        canvas.pack()

        canvas_width = pcr_teeth_canvas_width + 2
        canvas_height = pcr_teeth_canvas_height + 2

        ue = canvas.create_polygon(2, 2,
                                   canvas_width, 2,
                                   canvas_width / 2, canvas_height / 2,
                                   fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

        migi = canvas.create_polygon(canvas_width, 2,
                                     canvas_width, canvas_height,
                                     canvas_width / 2, canvas_height / 2,
                                     fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

        shita = canvas.create_polygon(canvas_width, canvas_height,
                                      2, canvas_height,
                                      canvas_width / 2, canvas_height / 2,
                                      fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

        hidari = canvas.create_polygon(2, canvas_height,
                                       2, 2,
                                       canvas_width / 2, canvas_height / 2,
                                       fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")