import tkinter
from AgPCR import AgPCR


def main():
    root = tkinter.Tk()
    root.geometry('1400x770')
    root.wm_title("agPCR")

    ag_pcr = AgPCR(root)
    ag_pcr.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
