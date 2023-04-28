from tkinter import *
from tkVideoPlayer import TkinterVideo
import file
import os

window = Tk()
window.title("Video")
window.geometry("500x500")
window.config(bg="orange")

heading = Label(window, text="Video", bg="red", fg="blue", font="none 24 bold")
heading.config(anchor=CENTER)
heading.pack()

def importFile():
    vfile = file.openFile()
    if vfile is not None:
        global filename
        filename = vfile.title()
        global videoplayer
        videoplayer = TkinterVideo(master=window, scaled=True)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()

importBtn = Button(window, text="Import", command=lambda:importFile())
importBtn.pack(side=TOP, pady=2)

playBtn = Button(window, text="Play", command=lambda:videoplayer.play())
playBtn.pack(side=TOP, pady=3)

pauseBtn = Button(window, text="Pause", command=lambda:videoplayer.pause())
pauseBtn.pack(side=TOP, pady=4)

stopBtn = Button(window, text="Stop", command=lambda:videoplayer.stop())
stopBtn.pack(side=TOP, pady=5)

# videoplayer = TkinterVideo(master=root, scaled=True)
#
# videoplayer.load(file.openFile())
#
# videoplayer.pack(expand=True, fill="both")
#
# videoplayer.play()

window.mainloop()