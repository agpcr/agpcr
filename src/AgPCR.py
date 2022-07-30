import tkinter
import widget


class AgPCR(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.view = widget.AgPCRView(self)
        self.view.grid(row=0, column=0)

        # PDPCR表示部:上下のコンポーネントのスペースを開ける
        self.spacer = tkinter.Frame(self)
        self.spacer.grid(row=1, column=0, pady=10)

        self.controller = widget.PCRController(self,
                                               is_missing_callback=self.is_missing_callback,
                                               on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                               on_change_teeth_plane_callback=self.on_change_teeth_plane_callback)
        self.controller.grid(row=2, column=0)

    def is_missing_callback(self, ev, fdi_number):
        self.view.on_missing(fdi_number)

    def on_change_probing_depth_callback(self, fdi_number, pd, planes):
        self.view.on_change_probing_depth(fdi_number, pd, planes)

    def on_change_teeth_plane_callback(self, fdi_number, planes, pd):
        self.view.on_change_teeth_plane(fdi_number, planes, pd)