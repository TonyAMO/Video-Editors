import tkinter as tk
from ttkwidgets import TimeLine

window = tk.Tk()
timeline = TimeLine(    #track formatting
    window,
    categories={str(key): {"text": "Category {}".format(key)} for key in range(0, 5)},
    height=100, extend=True
)
menu = tk.Menu(window, tearoff=False) #window open
menu.add_command(label="Some Action", command=lambda: print("Command Executed"))
timeline.tag_configure("1", right_callback=lambda *args: print(args), menu=menu, foreground="green",
                       active_background="yellow", hover_border=2, move_callback=lambda *args: print(args)) #track 1 changes color once clicked
timeline.create_marker("1", 1.0, 2.0, background="white", text="Change Color", tags=("1",), iid="1") #track 1
timeline.create_marker("2", 2.0, 3.0, background="green", text="Change Category", foreground="white", iid="2",
                       change_category=True) #track 2 can be move to different row
timeline.create_marker("3", 1.0, 2.0, text="Show Menu", change_category=True, tags=("1",)) # track 3 can change color when clicked and can be move to different category
#timeline.create_marker("4", 4.0, 5.0, text="Do nothing", move=False) #stays in place, cannot change color
timeline.draw_timeline()
timeline.grid() #creates timeline
window.after(2500, lambda: timeline.configure(marker_background="cyan")) #default background color for track 3
window.after(5000, lambda: timeline.update_marker("1", background="red")) #default background color for track 1
window.after(5000, lambda: print(timeline.time))
window.mainloop()
