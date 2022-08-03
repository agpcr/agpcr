import tkinter
from AgPCR import AgPCR


def main():
    root = tkinter.Tk()
    root.geometry('1400x450')
    root.wm_title("PCR")

    ag_pcr = AgPCR(root)
    ag_pcr.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
