import tkinter
from AgPCR import AgPCR

root = tkinter.Tk()
root.geometry('1400x770')
root.wm_title("agPCR")

agPCR = AgPCR(root)
agPCR.pack()

root.mainloop()

if __name__ == '__main__':
    print("hello")