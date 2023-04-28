#import
import tkinter
import numpy as np
import cv2
from tkinter import *
from moviepy.editor import *
from pygame import *
from file import *
from ttkwidgets import TimeLine
from tkVideoPlayer import TkinterVideo



#Functions
global videoplayer
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

        # videoplayer = TkinterVideo(master=root, scaled=True)
        videoplayer.load(final_clip)
        # videoplayer.pack(expand=True, fill="both", side=BOTTOM)
        # videoplayer.play()

        #videoplayer = TkinterVideo(master=root, scaled=True)
       #videoplayer.load(final_clip)
       #videoplayer.pack(expand=True, fill="both", side=BOTTOM)
        #videoplayer.play()


def mirror():
    global final_clip
    clip_mirror = final_clip.fx(vfx.mirror_y)
    final_clip = clip_mirror
    print("Mirroring Done!")

def resize():
    global final_clip
    w = int(input("add a width"))
    h = int(input("add a height"))
    clip_final = final_clip.resize(width=w, height=h)
    final_clip = clip_final
    print("Resizing Done!")

def speed_vfx():
    global final_clip
    print("Please enter the speed in which you wish to apply to the video (0.5 for half-speed, 2.0 for twice as fast): ")
    speed_input = float(input(""))
    clip_speed = final_clip.fx(vfx.speedx, speed_input)
    final_clip = clip_speed
    print("Speed Adjustment Done!")
def brightness_vfx():
    global final_clip
    print("Please specify if you wish to darken or brighten your clip (Less than 1.0 to darken, Greater than 1.0 to brighten): ")
    brightness = float(input(""))
    clip_brightness = final_clip.fx( vfx.colorx, brightness)
    final_clip = clip_brightness
    print("Brightness Adjustments Done!")

def foreground_removal():
    video = cv2.VideoCapture("C:\Datasets\stationary cam.mp4")

    FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

    # creating an array of frames from frames chosen above
    frames = []
    for frameOI in FOI:
        video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
        ret, frame = video.read()
        frames.append(frame)

    # calculate the average
    backgroundFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
    cv2.imshow("background only", backgroundFrame)
def background_removal():
    video = cv2.VideoCapture('C:\Datasets\MLB.mp4')
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while (1):
        ret, frame = video.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('fgmask', fgmask)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    video.release()
    cv2.destroyAllWindows()
def colorize():
    global final_clip
    print("Please specify luminosity (0-255), contrast (0-255), contrast threshold (0-127) values "
          "for colorizing your clip: ")
    red_input = int(input(""))
    green_input = int(input(""))
    blue_input = int(input(""))
    clip_colorize = final_clip.fx(vfx.lum_contrast, red_input, green_input, blue_input)
    final_clip = clip_colorize
    print("Colorize Adjustments Done!")

def trim():
    global final_clip
    print("Please specify the starting second and ending second that you wish to clip: ")
    start = int(input(""))
    end = int(input(""))
    clip_trim = final_clip.subclip(start, end)
    final_clip = clip_trim
    print("Trim Done!")


def export():
    global final_clip
    print("Please enter the file name: ")
    user_input = input("")
    clip_name = user_input + ".mp4"
    final_clip.write_videofile(clip_name, codec="libx264", audio_codec="aac")


#main screen

root = Tk()
root.title("Video editor")
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry('%dx%d' % (width, height))
root.geometry("850x200")
root.minsize(1700,700)
root.maxsize(1700,700)
#root.config(bg='#232323')


tn=5
tm=0

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


#mix
b=Button(root, text="remove all objects", relief=GROOVE, bg="#232323", fg="white", command=foreground_removal)
b.pack(side="left", anchor=NW,  padx=20)
b.config(width=8, height=3)

#mix
b=Button(root, text="Mix", relief=GROOVE, bg="#232323", fg="white", command=mix)
b.pack(side="left", anchor=NW,  padx=20)
b.config(width=8, height=3)

#mirror

b=Button(root, text="Mirror", relief=GROOVE, bg="#232323", fg="white", command=mirror)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

#resize

b=Button(root, text="Resize", relief=GROOVE, bg="#232323", fg="white", command=resize)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

#speed

b=Button(root, text="Speed", relief=GROOVE, bg="#232323", fg="white", command=speed_vfx)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

#darken/lighten

b=Button(root, text="Brightness", relief=GROOVE, bg="#232323", fg="white", command=brightness_vfx)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

#colorizing

b=Button(root, text="Colorizing", relief=GROOVE, bg="#232323", fg="white", command=colorize)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

#trim

b=Button(root, text="Trim", relief=GROOVE, bg="#232323", fg="white", command=trim)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

#audio

# b=Button(root, text="Audio", relief=GROOVE, bg="#232323", fg="white", command=audio_file)
# b.pack(side="left", padx=20)
# b.config(width=8, height=3)


#export

b=Button(root, text="Export", relief=GROOVE, bg="#232323", fg="white", command=export)
b.pack(side="left", anchor=NW, padx=20)
b.config(width=8, height=3)

tb=Button(root, text="add marker", relief=GROOVE, bg="#232323", fg="white", command=add_marker)
tb.pack(side="left", anchor=NW, padx=20)
tb.config(width=8, height=3)

tb=Button(root, text="delete marker", relief=GROOVE, bg="#232323", fg="white", command=delete_marker)
tb.pack(side="left", anchor=NW, padx=20)
tb.config(width=8, height=3)
menu = tk.Menu(root, tearoff=False) #window open


def importFile():
    vfile = openFile()
    if vfile is not None:
        global filename
        filename = vfile.title()
        videoplayer = TkinterVideo(master=root, scaled=True)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()

importBtn = Button(root, text="Import", command=lambda:importFile())
importBtn.pack(side=TOP, pady=2)

playBtn = Button(root, text="Play", command=lambda:videoplayer.play())
playBtn.pack(side=TOP, pady=3)

pauseBtn = Button(root, text="Pause", command=lambda:videoplayer.pause()())
pauseBtn.pack(side=TOP, pady=4)

stopBtn = Button(root, text="Stop", command=lambda:videoplayer.stop())
stopBtn.pack(side=TOP, pady=5)




timeline = TimeLine(    #track formatting
    root,
    categories={str(key): {"text": "Category {}".format(key)} for key in range(0, tn)},
    height=100, extend=True
)









timeline.tag_configure("1", right_callback=lambda *args: print(args), menu=menu, foreground="green",
                       active_background="yellow", hover_border=2, move_callback=lambda *args: print(args)) #track 1 changes color once clicked
timeline.create_marker("1", 1.0, 2.0, background="white", text="Change Color", tags=("1",), iid="1")        #track 1
timeline.create_marker("2", 2.0, 3.0, background="green", text="Change Category", foreground="white", iid="2",
                       change_category=True, image="logo.png")                                              #track 2 can be move to different row
timeline.create_marker("3", 1.0, 2.0, text="Show Menu", change_category=True, tags=("1",))                  # track 3 can change color when clicked and can be move to different category
timeline.draw_timeline()
timeline.pack(side=BOTTOM, anchor=NW) #creates timeline

#root.after(2500, lambda: timeline.configure(marker_background="cyan")) #default background color for track 3
#root.after(5000, lambda: timeline.update_marker("1", background="red")) #default background color for track 1
root.after(5000, lambda: print(timeline.time))

root.mainloop()