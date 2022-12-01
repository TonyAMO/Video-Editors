import file
import tkinter as tk
from tkinter import *
from file import *
from edit import *
import cgi

def doNothing():
    print('doo nothing')


window = Tk()
if __name__ == '__main__':
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry('%dx%d' % (width, height))
    window.title('Video Editor')

    menu = Menu(window)
    window.config(menu=menu)

    fileMenu = Menu(menu)
    app = fileButton()
    # menu.add_cascade(label="File",menu=fileMenu)
    # fileMenu.add_command(label='Import', command=fileButton.importFile(window))

    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)


    window.mainloop()