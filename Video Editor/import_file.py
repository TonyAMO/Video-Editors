import tkinter as tk
from tkinter import *
from tkinter import filedialog

from PIL import Image
from playsound import playsound

import time
import wave

import os

class fileButton(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Import', command=openFile)
        menubar.add_cascade(label='File', menu=fileMenu)
    def onExit(self):
        self.quit()

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\aojed\\Downloads",
                                          title='Import file',
                                          filetypes=(("images", "*.png"),
                                            ("videos", "*.mp4"),
                                            ('audio', "*.mp3")))
    if filepath.endswith(".png"):
        try:
            img = Image.open(filepath)
            img.show()
        except IOError:
            window = Tk()
            window.geometry("250x170")
            button = Button(text="OK")
            button.pack()
            T = Text(window, height=5, width=52)
            T.insert(END, "no image found")
            window.mainloop()
            print("no image found")
    elif filepath.endswith(".mp3"):
        # head_tail = os.path.split(filepath)
        # filepath_str = str(head_tail[0])+str(head_tail[1])
        # playsound(r'')
        print('Playing audio file')
    # file = open(filepath, 'r')
    # print(file.read())
    # file.close()
    #print(filepath)



#openFile()
window = Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry('%dx%d'%(width,height))
window.title('Video Editor')
app = fileButton()
window.mainloop()