#import
import tkinter
from tkinter import *
from moviepy.editor import *
from pygame import *
from file import openFile

#Functions




def import_clip():
    return VideoFileClip(openFile())

def mix():
    mix_input = Tk()
    mix_input.title("Mix videos")
    mix_input.geometry("600x400")
    label1 = tkinter.Label(mix_input, text="Enter amount of videos to mix", font=('calibre',10, 'bold'))
    label1.pack()
    entry1 = tkinter.Entry(mix_input, width=35)
    entry1.pack()
    def submit():
        i = entry1.get()
    button = Button(mix_input, text="Submit", command=lambda: [submit(), mix_input.destroy()])
    button.pack()

    mix_input.mainloop()
    # clip_1 = import_clip()
    # clip_2 = import_clip()
    # clip_3 = import_clip()
    clips = []
    #i = int(input("enter input: "))
    for c in range(0,i):
        clips.append(import_clip())
    final_clip=concatenate_videoclips(clips)
    final_clip.write_videofile("final_render.mp4")

def mirror():
    clip_mirror = import_clip().fx(vfx.mirror_x)
    clip_mirror.write_videofile("final_render.mp4")

def resize():
    r=float(input("Enter your resize: "))
    #w=int(input("Enter your width: "))
    #h=int(input("Enter your height: "))
    clip_resize=import_clip().resize(r).margin(top=1)
    #clip_resize.preview()
    clip_resize.write_videofile("final_render.mp4")

def speed_vfx():
    speed = float(input("Enter your speed: "))
    clip_speed = import_clip().fx(vfx.speedx, speed)
    clip_speed.write_videofile("final_render.mp4")

def color_vfx():
    color = float(input("Value of darkness: "))
    clip_color = import_clip().fx(vfx.colorx, color)
    clip_color.write_videofile("final_render.mp4")

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

#main screen

root = Tk()
root.title("Video editor")
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry('%dx%d' % (width, height))
root.geometry("750x200")
root.minsize(750,200)
root.maxsize(750,200)
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

b=Button(root, text="Color", relief=GROOVE, bg="#232323", fg="white", command=color_vfx)
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

root.mainloop()