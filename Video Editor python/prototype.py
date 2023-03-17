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
    global final_clip
    clip_mirror = import_clip().fx(vfx.mirror_y)
    print("please type the file name")
    user_input = input("")
    clip_name = user_input + ".mp4"
    clip_mirror.write_videofile(clip_name, codec="libx264")
    final_clip = clip_mirror

def resize():
    clip = import_clip()
    w = int(input("add a width"))
    h = int(input("add a height"))
    clip_final = clip.resize(width=w, height=h)
    clip_final.write_videofile("test_resize.mp4", codec="libx264", audio_codec="aac")

def speed_vfx():
    print("Please enter the speed in which you wish to apply to the video (0.5 for half-speed, 2.0 for twice as fast): ")
    speed_input = float(input(""))
    clip_speed = import_clip().fx(vfx.speedx, speed_input)
    print("Please type the file name:")
    user_input = input("")
    clip_name = user_input + ".mp4"
    clip_speed.write_videofile(clip_name, codec="libx264", audio_codec="aac")

def brightness_vfx():
    clip = import_clip()
    print("Please specify if you wish to darken or brighten your clip (Less than 1.0 to darken, Greater than 1.0 to brighten): ")
    brightness = float(input(""))
    clip_brightness = clip.fx( vfx.colorx, brightness)
    print("Please type the file name:")
    user_input = input("")
    clip_name = user_input + ".mp4"
    clip_brightness.write_videofile(clip_name, codec="libx264", audio_codec="aac")


def trim():
    clip = import_clip()
    print("Please specify the starting second and ending second that you wish to clip: ")
    start = int(input(""))
    end = int(input(""))
    clip_trim = clip.subclip(start, end)
    print("Please type the file name:")
    user_input = input("")
    clip_name = user_input + ".mp4"
    clip_trim.write_videofile(clip_name, codec="libx264", audio_codec="aac")


def export():
    global final_clip
    exportFile(final_clip)

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

#darken/lighten

b=Button(root, text="Brightness", relief=GROOVE, bg="#232323", fg="white", command=brightness_vfx)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#trim

b=Button(root, text="Trim", relief=GROOVE, bg="#232323", fg="white", command=trim)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#audio

# b=Button(root, text="Audio", relief=GROOVE, bg="#232323", fg="white", command=audio_file)
# b.pack(side="left", padx=20)
# b.config(width=8, height=3)

#export

b=Button(root, text="Export", relief=GROOVE, bg="#232323", fg="white", command=export)
b.pack(side="left", padx=20)
b.config(width=8, height=3)



root.mainloop()