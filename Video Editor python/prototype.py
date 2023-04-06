#import
import tkinter
from tkinter import *
from moviepy.editor import *
from pygame import *
from file import *
from ttkwidgets import TimeLine


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
    clip_speed.write_videofile(clip_name, codec="libx264")

def color_vfx():
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
    global final_clip
    trim_input = Tk()

    trim_input.title("Trim video")
    trim_input.geometry("600x400")
    label1 = tkinter.Label(trim_input, text="Enter starting point", font=('calibre', 10, 'bold'))
    label1.pack()
    entry1 = tkinter.Entry(trim_input, width=35)
    entry1.pack()
    label2 = tkinter.Label(trim_input, text="Enter ending point", font=('calibre', 10, 'bold'))
    label2.pack()
    entry2 = tkinter.Entry(trim_input, width=35)
    entry2.pack()

    def submit():
        global start, end
        e1 = entry1.get()
        e2 = entry2.get()
        start = int(e1)
        end = int(e2)
    button = Button(trim_input, text="Submit", command=lambda: [submit(), trim_input.destroy(), trim_input.quit()])
    button.pack()
    trim_input.mainloop()
    # starting=int(input("Enter starting point here: "))
    # ending = int(input("Enter ending point here: "))
    if (start != None or end!=None) and final_clip == None:
        final_clip = import_clip().subclip(start,end)

# def audio_file():
#     import moviepy.editor as mpe
#     audioclip = mpe.AudioFileClip(import_clip())
#     videoclip = mpe.videoclip.set_audio(audioclip)
#     final_clip = videoclip.set_audio(audioclip)
#     final_clip.write_videofile("final_render.mp4")

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
root.minsize(1700,400)
root.maxsize(1700,400)
#root.config(bg='#232323')


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

# b=Button(root, text="Audio", relief=GROOVE, bg="#232323", fg="white", command=audio_file)
# b.pack(side="left", padx=20)
# b.config(width=8, height=3)

#export

b=Button(root, text="Export", relief=GROOVE, bg="#232323", fg="white", command=export)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

tn=5
tm=0

timeline = TimeLine(    #track formatting
    root,
    categories={str(key): {"text": "Category {}".format(key)} for key in range(0, tn)},
    height=100, extend=True, padding=100
)
menu = tk.Menu(root, tearoff=False) #window open

def add_marker():
    global tn, tm, timeline
    tm=tm+1
    timeline.create_marker(str(tm), 1.0, 2.0, text="new category", foreground="white", change_category=True)

def delete_marker():
    global tn, tm, timeline
    timeline.destroy()
    timeline = TimeLine(  # track formatting
        root,
        categories={str(key): {"text": "Category {}".format(key)} for key in range(0, tn)},
        height=100, extend=True
    )

tb=Button(root, text="add marker", relief=GROOVE, bg="#232323", fg="white", command=add_marker)
tb.pack(side="left", padx=20)
tb.config(width=8, height=3)

tb=Button(root, text="delete marker", relief=GROOVE, bg="#232323", fg="white", command=delete_marker)
tb.pack(side="left", padx=20)
tb.config(width=8, height=3)


timeline.tag_configure("1", right_callback=lambda *args: print(args), menu=menu, foreground="green",
                       active_background="yellow", hover_border=2, move_callback=lambda *args: print(args)) #track 1 changes color once clicked
timeline.create_marker("1", 1.0, 2.0, background="white", text="Change Color", tags=("1",), iid="1")        #track 1
timeline.create_marker("2", 2.0, 3.0, background="green", text="Change Category", foreground="white", iid="2",
                       change_category=True, image="logo.png")                                              #track 2 can be move to different row
timeline.create_marker("3", 1.0, 2.0, text="Show Menu", change_category=True, tags=("1",))                  # track 3 can change color when clicked and can be move to different category
timeline.draw_timeline()
timeline.pack() #creates timeline

#root.after(2500, lambda: timeline.configure(marker_background="cyan")) #default background color for track 3
#root.after(5000, lambda: timeline.update_marker("1", background="red")) #default background color for track 1
root.after(5000, lambda: print(timeline.time))

root.mainloop()