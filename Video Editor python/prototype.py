#import
import tkinter
import directory
import numpy as np
import cv2
from tkinter import *
from moviepy.editor import *
from pygame import *
from file import *
from ttkwidgets import TimeLine
from tkVideoPlayer import TkinterVideo





#Functions

exportPath = None
final_clip= None
edited_clip=None
videoplayer = None

def replace_player(player):
    global exportPath
    global videoplayer
    global final_clip
    # delete the existing player
    player.pack_forget()
    final_clip = open(exportPath, 'r')
    # create a new player and pack it into the window
    player2 = TkinterVideo(master=root, scaled=True, keep_aspect=True)
    if final_clip is not None:
        player2.load(r"{}".format(exportPath))
        player2.pack(expand=True, fill="both")
        player2.play()


def importFile():
    global exportPath
    global videoplayer
    global final_clip
    final_clip = open(exportPath, 'r')
    videoplayer = TkinterVideo(master=root, scaled=True, keep_aspect=True)
    if videoplayer.winfo_ismapped():
        replace_player(videoplayer)
    if final_clip is not None and not videoplayer.winfo_ismapped():
        videoplayer.load(r"{}".format(exportPath))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()

def import_clip():
    global edited_clip
    edited_clip=VideoFileClip(openFile())
    return edited_clip

def mix():
    global final_clip
    global edited_clip
    global exportPath
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

        edited_clip=concatenate_videoclips(clips)
        exportPath = directory.path() + "\\test.mp4"
        edited_clip.write_videofile(filename=exportPath, codec="libx264", audio_codec="aac")
        importFile()


def mirror():
    global final_clip
    global edited_clip
    clip_mirror = edited_clip.fx(vfx.mirror_y)
    edited_clip = clip_mirror
    exportPath = directory.path() + "\\test.mp4"
    edited_clip.write_videofile(filename=exportPath, codec="libx264", audio_codec="aac")
    importFile()
    print("Mirroring Done!")

def resize():
    global final_clip
    w = int(input("add a width"))
    h = int(input("add a height"))
    clip_final = final_clip.resize(width=w, height=h)
    final_clip = clip_final
    print("Resizing Done!")
    exportPath = directory.path() + "\\test.mp4"
    final_clip.write_videofile(filename=exportPath, codec="libx264", audio_codec="aac")
    importFile()
    print("Mirroring Done!")

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
    clip_brightness = final_clip.fx(vfx.colorx, brightness)
    final_clip = clip_brightness
    print("Brightness Adjustments Done!")

def foreground_removal():
    video = cv2.VideoCapture(exportPath)

    FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

    # creating an array of frames from frames chosen above
    frames = []
    for frameOI in FOI:
        video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
        ret, frame = video.read()
        frames.append(frame)

    # calculate the average
    backgroundFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
    cv2.imshow("Foreground only", backgroundFrame)
def background_removal():
    video = cv2.VideoCapture(exportPath)
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while (1):
        ret, frame = video.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('Background Mask', fgmask)

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

def fadeinfadeout():
    print("You can concatenate up to 3 clips using the fade-in/out transition feature.")
    choice = int(input("Please specify number of clips to concatenate with a fade-in/out transition feature."))
    if choice == 1:
        clip1 = import_clip().fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
        clipname = input("Please enter the file name: ")
        clip_name = clipname + ".mp4"
        clip1.write_videofile(clip_name, codec="libx264", audio_codec="aac")
    if choice == 2:
        clip1 = import_clip().fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
        clip2 = import_clip().fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
        combined = concatenate_videoclips([clip1, clip2])
        clipname = input("Please enter the file name: ")
        clip_name = clipname + ".mp4"
        combined.write_videofile(clip_name, codec="libx264", audio_codec="aac")
    if choice == 3:
        clip1 = import_clip().fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
        clip2 = import_clip().fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
        clip3 = import_clip().fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
        combined = concatenate_videoclips([clip1, clip2, clip3])
        clipname = input("Please enter the file name: ")
        clip_name = clipname + ".mp4"
        combined.write_videofile(clip_name, codec="libx264", audio_codec="aac")

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


button_frame = tk.Frame(root)
button_frame.pack(side="top", padx=10, pady=10)

#foreground
b=Button(button_frame, text="FG\nRemoval", relief=GROOVE, bg="#232323", fg="white", command=foreground_removal)
b.pack(side="left",  padx=20)
b.config(width=8, height=3)

#background
b=Button(button_frame, text="BG\nRemoval", relief=GROOVE, bg="#232323", fg="white", command=background_removal)
b.pack(side="left",  padx=20)
b.config(width=8, height=3)

#mix
b=Button(button_frame, text="Mix", relief=GROOVE, bg="#232323", fg="white", command=mix)
b.pack(side="left",  padx=20)
b.config(width=8, height=3)

#mirror

b=Button(button_frame, text="Mirror", relief=GROOVE, bg="#232323", fg="white", command=mirror)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#resize

b=Button(button_frame, text="Resize", relief=GROOVE, bg="#232323", fg="white", command=resize)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#speed

b=Button(button_frame, text="Speed", relief=GROOVE, bg="#232323", fg="white", command=speed_vfx)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#darken/lighten

b=Button(button_frame, text="Brightness", relief=GROOVE, bg="#232323", fg="white", command=brightness_vfx)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#colorizing

b=Button(button_frame, text="Colorizing", relief=GROOVE, bg="#232323", fg="white", command=colorize)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#trim

b=Button(button_frame, text="Trim", relief=GROOVE, bg="#232323", fg="white", command=trim)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#fade-in/out

b=Button(button_frame, text="Fade-\nIn/Out", relief=GROOVE, bg="#232323", fg="white", command=fadeinfadeout)
b.pack(side="left", padx=20)
b.config(width=8, height=3)


#export

b=Button(button_frame, text="Export", relief=GROOVE, bg="#232323", fg="white", command=export)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

tb=Button(button_frame, text="add\nmarker", relief=GROOVE, bg="#232323", fg="white", command=add_marker)
tb.pack(side="left", padx=20)
tb.config(width=8, height=3)

tb=Button(button_frame, text="delete\nmarker", relief=GROOVE, bg="#232323", fg="white", command=delete_marker)
tb.pack(side="left", padx=20)
tb.config(width=8, height=3)
menu = tk.Menu(root, tearoff=False) #window open


button_frame_1 = tk.Frame(root)
button_frame_1.pack(side="top", padx=10, pady=10)


playBtn = Button(button_frame_1, text="Play", command=lambda:videoplayer.play)
playBtn.pack(side='left', padx=5)

pauseBtn = Button(button_frame_1, text="Pause", command=lambda:videoplayer.pause)
pauseBtn.pack(side='left', padx=5)

stopBtn = Button(button_frame_1, text="Stop", command=lambda:videoplayer.stop)
stopBtn.pack(side='left', padx=5)




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
timeline.pack(side="bottom") #creates timeline

#root.after(2500, lambda: timeline.configure(marker_background="cyan")) #default background color for track 3
#root.after(5000, lambda: timeline.update_marker("1", background="red")) #default background color for track 1
root.after(5000, lambda: print(timeline.time))

root.mainloop()