import tkinter as tk
from tkinter import *
from tkinter import filedialog

from PIL import Image
from playsound import playsound

import time
import wave

import os



def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\aojed\\Downloads",
                                          title='Import file',
                                          filetypes=(("images", "*.png"),
                                            ("all files", "*.*"),
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


window = Tk()
window.geometry("250x170")

no_image = Label(window, text='No image found')
no_image.config(font =("Courier", 14))
button = Button(text="OK", command=window.destroy())
no_image.pack()
button.pack()
tk.mainloop()
# openFile()
# window = Tk()
# button = Button(text="Open", command=openFile)
# button.pack()
# window.mainloop()