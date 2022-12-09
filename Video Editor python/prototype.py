#import
import tkinter
from tkinter import *
from moviepy.editor import *
from pygame import *
from file import *

#Functions

final_clip= None


def import_clip():
    return VideoFileClip(openFile())

def mix():
    global final_clip
    mix_input = Tk()

    mix_input.title("Mix videos")
    mix_input.geometry("600x400")
    label1 = tkinter.Label(mix_input, text="Enter amount of videos to mix", font=('calibre',10, 'bold'))
    label1.pack()
    def submit():
        global i
        e = entry1.get()
        print(e)
        i = int(e)
        print(i)
    entry1 = tkinter.Entry(mix_input, width=35)
    entry1.pack()
    button = Button(mix_input, text="Submit", command=lambda: [submit(), mix_input.destroy(), mix_input.quit()])
    button.pack()
    mix_input.mainloop()
    clips = []
    #i = int(input("enter input: "))
    if i != None and final_clip == None:
        for c in range(0,i):
            clips.append(import_clip())

        final_clip=concatenate_videoclips(clips)


def mirror():
    clip_mirror = import_clip().fx(vfx.mirror_x)
    clip_mirror.write_videofile("baby.mp4")

def resize():
    global final_clip
    rsz_input = Tk()

    rsz_input.title("Mix videos")
    rsz_input.geometry("600x400")
    label1 = tkinter.Label(rsz_input, text="Enter resize amount", font=('calibre', 10, 'bold'))
    label1.pack()

    def submit():
        global r
        e = entry1.get()
        print(e)
        r = float(e)

    entry1 = tkinter.Entry(rsz_input, width=35)
    entry1.pack()
    button = Button(rsz_input, text="Submit", command=lambda: [submit(), rsz_input.destroy(), rsz_input.quit()])
    button.pack()
    rsz_input.mainloop()
    if r!=None and final_clip==None:
        final_clip=import_clip().resize(r).margin(top=1)

def speed_vfx():
    global final_clip
    spd_input = Tk()

    spd_input.title("Speed up/down video")
    spd_input.geometry("600x400")
    label1 = tkinter.Label(spd_input, text="Enter speed", font=('calibre', 10, 'bold'))
    label1.pack()
    def submit():
        global sp
        e = entry1.get()
        print(e)
        sp = float(e)

    entry1 = tkinter.Entry(spd_input, width=35)
    entry1.pack()
    button = Button(spd_input, text="Submit", command=lambda: [submit(), spd_input.destroy(), spd_input.quit()])
    button.pack()
    spd_input.mainloop()
    if sp != None and final_clip == None:
        final_clip = import_clip().fx(vfx.speedx, sp)

def color_vfx():
    #color = float(input("Value of darkness: "))
    global final_clip
    col_input = Tk()

    col_input.title("Brightness")
    col_input.geometry("600x400")
    label1 = tkinter.Label(col_input, text="Enter brightness", font=('calibre', 10, 'bold'))
    label1.pack()

    def submit():
        global col
        e = entry1.get()
        print(e)
        col = float(e)

    entry1 = tkinter.Entry(col_input, width=35)
    entry1.pack()
    button = Button(col_input, text="Submit", command=lambda: [submit(), col_input.destroy(), col_input.quit()])
    button.pack()
    col_input.mainloop()
    if col != None and final_clip == None:
        final_clip = import_clip().fx(vfx.colorx, col)

def trim():
    starting=int(input("Enter starting point here: "))
    ending = int(input("Enter ending point here: "))
    clip_trim = import_clip().subclip(starting,ending)
    clip_trim.write_videofile("final_render.mp4")

def audio_file():
    import moviepy.editor as mpe
    audioclip = mpe.AudioFileClip(import_clip())
    videoclip = mpe.videoclip.set_audio(audioclip)
    final_clip = videoclip.set_audio(audioclip)
    final_clip.write_videofile("final_render.mp4")

def export():
    global final_clip
    exportFile(final_clip)
    # exp_input = Tk()
    #
    # exp_input.title("Export video")
    # exp_input.geometry("600x400")
    # label1 = tkinter.Label(exp_input, text="Enter name of video", font=('calibre', 10, 'bold'))
    # label1.pack()
    # def submit():
    #     global name
    #     e = entry1.get()
    #     name = str(e)+".mp4"
    #
    # entry1 = tkinter.Entry(exp_input, width=35)
    # entry1.pack()
    # button = Button(exp_input, text="Submit", command=lambda: [submit(), exp_input.destroy(), exp_input.quit()])
    # button.pack()
    # exp_input.mainloop()
    #
    # final_clip.write_videofile(name)

#main screen

root = Tk()
root.title("Video editor")
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry('%dx%d' % (width, height))
root.geometry("850x200")
root.minsize(850,200)
root.maxsize(850,200)
root.config(bg='#232323')


#mix
b=Button(root, text="Mix", relief=GROOVE, bg="#232323", fg="white", command=mix)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#mirror

b=Button(root, text="Mirror", relief=GROOVE, bg="#232323", fg="white", command=mirror)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#resize

b=Button(root, text="Resize", relief=GROOVE, bg="#232323", fg="white", command=resize)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#speed

b=Button(root, text="Speed", relief=GROOVE, bg="#232323", fg="white", command=speed_vfx)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#color

b=Button(root, text="Brightness", relief=GROOVE, bg="#232323", fg="white", command=color_vfx)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#trim

b=Button(root, text="Trim", relief=GROOVE, bg="#232323", fg="white", command=trim)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#audio

b=Button(root, text="Audio", relief=GROOVE, bg="#232323", fg="white", command=audio_file)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#export

b=Button(root, text="Export", relief=GROOVE, bg="#232323", fg="white", command=export)
b.pack(side="left", padx=20)
b.config(width=8, height=3)



root.mainloop()