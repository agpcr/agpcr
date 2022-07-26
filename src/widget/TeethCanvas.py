import tkinter


class TeethCanvas(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        pcr_teeth_canvas_width = 50
        pcr_teeth_canvas_height = 50

        self.canvas = tkinter.Canvas(self, width=pcr_teeth_canvas_width, height=pcr_teeth_canvas_height, bg='light yellow')
        self.canvas.pack()

        canvas_width = pcr_teeth_canvas_width + 2
        canvas_height = pcr_teeth_canvas_height + 2

        self.ue = self.canvas.create_polygon(2, 2,
                                   canvas_width, 2,
                                   canvas_width / 2, canvas_height / 2,
                                   fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

        self.migi = self.canvas.create_polygon(canvas_width, 2,
                                     canvas_width, canvas_height,
                                     canvas_width / 2, canvas_height / 2,
                                     fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

        self.shita = self.canvas.create_polygon(canvas_width, canvas_height,
                                      2, canvas_height,
                                      canvas_width / 2, canvas_height / 2,
                                      fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

        self.hidari = self.canvas.create_polygon(2, canvas_height,
                                       2, 2,
                                       canvas_width / 2, canvas_height / 2,
                                       fill='white', outline='black', width=2.0, joinstyle=tkinter.BEVEL, tags=str(id) + "_l")

    def toggle_missing(self, is_missing):
        if is_missing:
            self.canvas.itemconfigure(self.ue, fill='gray')
            self.canvas.itemconfigure(self.migi, fill='gray')
            self.canvas.itemconfigure(self.shita, fill='gray')
            self.canvas.itemconfigure(self.hidari, fill='gray')
        else:
            self.canvas.itemconfigure(self.ue, fill='white')
            self.canvas.itemconfigure(self.migi, fill='white')
            self.canvas.itemconfigure(self.shita, fill='white')
            self.canvas.itemconfigure(self.hidari, fill='white')