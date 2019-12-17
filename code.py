import pygame
from tkinter import *
import os

window = Tk()
window.geometry("400x150")

pygame.mixer.init()
n=0
def startstop():
    global n
    n=n+1
    if n==1:
        songname = song_box.get()
        pygame.mixer.music.load(songname)
        pygame.mixer.music.play(0)
    elif(n%2)==0:
        pygame.mixer.music.pause()
    elif(n%2)!=0:
        pygame.mixer.music.unpause()

l1 = Label(window, text="Music Player", font="times 20")
l1.grid(row=1, column=1)

b1=Button(window,text="Start",width='10',command=startstop)
b1.grid(row=4,column=1)

b2=Button(window,text="Pause",width='10')
b2.grid(row=5,column=1)
b2=Button(window,text="Resume",width='10')
b2.grid(row=6,column=1)

songs = os.listdir()
song_box = StringVar(window)
song_box.set("select songs")
menu = OptionMenu(window,song_box,*songs)
menu.grid(row=4,column=4)

window.mainloop()
