import tkinter as tk
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk
import numpy as np
import cv2
import moviepy.editor as mpe
from playsound import playsound

import time
import wave

import os
#window = Tk()
class fileButton(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Import', command=self.importFile)
        menubar.add_cascade(label='File', menu=fileMenu)

    #File > Import
    def importFile(self):
        filePath = openFile()
        if filePath.endswith(".png"): #import image
            imgFile = ImageTk.PhotoImage(Image.open(filePath))
            label = tk.Label(image=imgFile)
            label.image = imgFile
            label.place(x=10,y=100)
        elif filePath.endswith(".mp4"): #import video
            vidFile = cv2.VideoCapture(filePath)
            while(vidFile.isOpened()):
                ret, frame = vidFile.read()
                if ret == True:
                    cv2.imshow('Frame', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
            vidFile.release()
            cv2.destroyAllWindows()
        elif filePath.endswith(".mp3"): #imput audio
            audioclip = mpe.AudioFileClip(filePath)
        else:
            return

    def onExit(self):
        self.quit()

#opens file navigation
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\aojed\\Downloads",
                                          title='Import file',
                                          filetypes=(("images", "*.png"),
                                            ("videos", "*.mp4"),
                                            ('audio', "*.mp3")))
    if filepath.endswith(".png"):
        try:
            return filepath
        except IOError:
            err_window = Tk()
            err_window.geometry("250x170")
            button = Button(text="OK")
            button.pack()
            T = Text(err_window, height=5, width=52)
            T.insert(END, "no image found")
            err_window.mainloop()
            print("no image found")
    elif filepath.endswith(".mp3"):
        try:
            return filepath
        except IOError:
            err_window = Tk()
            err_window.geometry("250x170")
            button = Button(text="OK")
            button.pack()
            T = Text(err_window, height=5, width=52)
            T.insert(END, "no image found")
            err_window.mainloop()
            print("no audio found")
    elif filepath.endswith(".mp4"):
        try:
            return filepath
        except IOError:
            err_window = Tk()
            err_window.geometry("250x170")
            button = Button(text="OK")
            button.pack()
            T = Text(err_window, height=5, width=52)
            T.insert(END, "no video found")
            err_window.mainloop()
    else:
        return None
    # file = open(filepath, 'r')
    # print(file.read())
    # file.close()
    #print(filepath)



#openFile()

