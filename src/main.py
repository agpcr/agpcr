import tkinter
from src import widget

root = tkinter.Tk()
root.geometry('300x200')


controller = widget.PCRController(root)
controller.pack()


root.mainloop()

if __name__ == '__main__':
    print("hello")