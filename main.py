# music player app

from tkinter import *
from commands import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

def open_folder_func():
    for i in open_folder():
        if i.endswith(".mp3"):
            playlist.insert(END, i)

def play_btn():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(music_name)
    mixer.music.play()
    music_lbl.config(text=music_name[0:-4])

root = Tk()
root.title("Music Player->Anon Anderson")
root.geometry("920x670+290+85")
root.config(bg="#0f1a2b")
root.resizable(False,False)
mixer.init()

# all the fonts styles
font1 = ("arial", 10, "bold")
font2 = ("arial", 10, "italic")

# icon placements
img_ico = PhotoImage(file="logo.png")
root.iconphoto(False, img_ico)
# Header image
h_img = PhotoImage(file="top.png")
Label(root, image=h_img, bg="#0f1a2b").pack()
# header logo
h_logo = PhotoImage(file="logo.png")
Label(root, image=h_logo, bg="#0f1a2b").place(x=65, y=108)
# play button
play_button = PhotoImage(file="play.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, activebackground="#0f1a2b", command=play_btn).place(x=100, y=400)

# stop button
stop_button = PhotoImage(file="stop.png")
Button(root, image=stop_button, bg="#0f1a2b", bd=0, activebackground="#0f1a2b", command=mixer.music.stop).place(x=30, y=500)

# resume button
resume_button = PhotoImage(file="resume.png")
Button(root, image=resume_button, bg="#0f1a2b", bd=0, activebackground="#0f1a2b", command=mixer.music.unpause).place(x=115, y=500)

# pause button
pause_button = PhotoImage(file="pause.png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, activebackground="#0f1a2b", command=mixer.music.pause).place(x=200, y=500)

# music display area
music_disp = PhotoImage(file="menu.png")
Label(root, image=music_disp, bg="#0f1a2b", bd=0).pack(padx=10, pady=50, side=RIGHT)

# label
music_lbl = Label(root, text="", font=font2, fg="white", bg="#0f1a2b")
music_lbl.place(x=60, y=340)

# music frame
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=250)

# music frame buttons
Button(root, text="open folder", width=15, height=2, font=font1, fg="white", bg="#21b3de", command=open_folder_func).place(x=330, y=300)
scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=font2, bg="#333333", fg="grey", selectbackground="lightblue",
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
