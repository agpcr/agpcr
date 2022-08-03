import tkinter
import widget


class AgPCR(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        sub_win = tkinter.Toplevel()
        sub_win.wm_title("agPCR")
        sub_win.geometry("1400x330")
        self.view = widget.AgPCRView(sub_win)
        self.view.pack()

        self.controller = widget.PCRController(self,
                                               on_change_missing_callback=self.on_change_missing_callback,
                                               on_change_probing_depth_callback=self.on_change_probing_depth_callback,
                                               on_change_teeth_plane_callback=self.on_change_teeth_plane_callback)
        self.controller.pack()

    def on_change_missing_callback(self, ev, fdi_number):
        self.view.on_change_missing(fdi_number)

    def on_change_probing_depth_callback(self, fdi_number, pd, planes):
        self.view.on_change_probing_depth(fdi_number, pd, planes)

    def on_change_teeth_plane_callback(self, fdi_number, planes, pd):
        self.view.on_change_teeth_plane(fdi_number, planes, pd)
