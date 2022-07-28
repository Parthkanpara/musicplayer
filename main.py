import tkinter
from tkinter import *
import fnmatch
import os

from pygame import mixer

window = tkinter.Tk()
window.geometry("540x420")
window.title("music")
icon = PhotoImage(file='music.png')
window.config(background="#737CA1")
window.iconphoto(True, icon)


rootpath = "C:\\Users\LENOVO\Music"
pattern = "*.mp3"

mixer.init()

prew_img = tkinter.PhotoImage(file="prev_img.png")
stop_img = tkinter.PhotoImage(file="stop_img.png")
play_img = tkinter.PhotoImage(file="play_img.png")
pause_img = tkinter.PhotoImage(file="pause_img.png")
next_img = tkinter.PhotoImage(file="next_img.png")



def play():
    label.config(text=playlist.get("anchor"))
    mixer.music.load(rootpath + "\\" + playlist.get("anchor"))
    mixer.music.play()

def stop():
    label.config(text=playlist.get("anchor"))
    mixer.music.load(rootpath + "\\" + playlist.get("anchor"))
    mixer.music.stop()

def pause():

    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
        pauseButton["bg"] = "green"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"
        pauseButton["bg"] = "red"
def next():
    nextsng = playlist.curselection()
    nextsng =nextsng[0] + 1
    next_songname = playlist.get(nextsng)
    label.config(text=next_songname)

    mixer.music.load(rootpath + "\\" + next_songname)
    mixer.music.play()

    playlist.select_clear(0, 'end')
    playlist.activate(nextsng)
    playlist.select_set(nextsng)

def previous():
    prevsng = playlist.curselection()
    prevsng =prevsng[0] - 1
    prev_songname = playlist.get(prevsng)
    label.config(text=prev_songname)

    mixer.music.load(rootpath + "\\" + prev_songname)
    mixer.music.play()

    playlist.select_clear(0, 'end')
    playlist.activate(prevsng)
    playlist.select_set(prevsng)


#for create list of
playlist = Listbox(window, selectmode=SINGLE, bg='#737CA1', fg="white", font=('arial', 15), width=100, selectbackground="DodgerBlue2")
playlist.pack(padx=15,pady=15)


label = tkinter.Label(window, text = '',bg='#737CA1', fg="white", font=('arial', 15))
label.pack(pady = 15)

top = tkinter.Frame(window, bg='#737CA1')
top.pack(padx=10, pady=5, anchor='center')


prevButton = tkinter.Button(window, text="prev", image=prew_img,borderwidth=2,command=previous)
prevButton.pack(pady=15, in_=top, side='left')
stopButton = tkinter.Button(window, text="stop", image=stop_img,borderwidth=2,command=stop)
stopButton.pack(pady=15, in_=top, side='left')
playButton = tkinter.Button(window, text="play", image=play_img,borderwidth=2, command=play)
playButton.pack(pady=15, in_=top, side='left')
pauseButton = tkinter.Button(window, text="pause", image=pause_img,borderwidth=2,command=pause)
pauseButton.pack(pady=15, in_=top, side='left')
nextButton = tkinter.Button(window, text="next", image=next_img,borderwidth=2,command=next)
nextButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        playlist.insert('end', filename)
window.mainloop()
