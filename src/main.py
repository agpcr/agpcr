import tkinter
from src import widget

root = tkinter.Tk()
root.geometry('1400x660')


controller = widget.PCRController(root)
controller.pack()


root.mainloop()

if __name__ == '__main__':
    print("hello")