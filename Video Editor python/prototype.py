#import
from tkinter import *
from moviepy.editor import *
from pygame import *
from file import openFile



#Functions

final_product = input('End File Name:\n ')

def import_clip():
    return VideoFileClip(openFile())

def mix():
    clips =[]
    i = int(input("Enter number of files you are choosing to mix: "))
    for c in range(0,i):
        clips.append(import_clip())
    final_clip=concatenate_videoclips(clips)
    final_clip.write_videofile(final_product)

def mirror():
    clip_mirror = import_clip().fx(vfx.mirror_x)
    clip_mirror.write_videofile(final_product)

def resize():
    r=float(input("Enter your resize: "))
    #w=int(input("Enter your width: "))
    #h=int(input("Enter your height: "))
    clip_resize=import_clip().resize(r).margin(top=1)
    #clip_resize.preview()
    clip_resize.write_videofile(final_product)

def speed_vfx():
    speed = float(input("Enter your output speed: "))
    clip_speed = import_clip().fx(vfx.speedx, speed)
    clip_speed.write_videofile(final_product)

def color_vfx():
    color = float(input("Value of darkness: "))
    clip_color = import_clip().fx(vfx.colorx, color)
    clip_color.write_videofile(final_product)

def trim():
    starting=int(input("Enter starting point here: "))
    ending = int(input("Enter ending point here: "))
    clip_trim = import_clip().subclip(starting,ending)
    clip_trim.write_videofile(final_product)

def audio_file():
    import moviepy.editor as mpe
    audioclip = mpe.AudioFileClip(import_clip())
    videoclip = mpe.videoclip.set_audio(audioclip)
    final_clip = videoclip.set_audio(audioclip)
    final_clip.write_videofile(final_product)

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