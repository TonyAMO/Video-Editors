import tkinter as tk
from tkinter import *
from import_file import *

window = Tk()
if __name__ == '__main__':
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry('%dx%d' % (width, height))
    window.title('Video Editor')
    app = fileButton()
    window.mainloop()