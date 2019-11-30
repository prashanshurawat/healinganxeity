import tkinter 
#from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image
def song1():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=cxjvTXo9WWM')

def song2():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=j5-yKhDd64s')

def song3():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=IcrbM1l_BoI')

def song4():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=nvlTJrNJ5lA')

def song5():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=fdubeMFwuGs')

def song6():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=jHNNMj5bNQw')

def song7():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=u3h1DvwH6yM')

def song8():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=t6MeeKrDIlM')

def song9():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=Ax0G_P2dSBw')

def song10():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=f0tjpwW4rzM')

def song11():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=p9DQINKZxWE')

songs = tkinter.Tk()
songs.geometry("1920x1080")

    
    
a = tkinter.Button(songs, text = 'UNSTOPPABLE', command = song1)
a.grid(column=0,row=1)
a.place(x=500,y=10)
    
    
b = tkinter.Button(songs, text = 'NOT AFRAID', command = song2)
b.grid(column=1,row=2)
b.place(x=300,y=100) 
    
    
c = tkinter.Button(songs, text = 'WAKE ME UP', command = song3)
c.grid(column=6,row=15)
c.place(x=600,y=150) 
    
    
c = tkinter.Button(songs, text = "I WON'T BACK DOWN", command = song4)
c.grid(column=10,row=9)
c.place(x=550,y=100) 
    
    
d = tkinter.Button(songs, text = 'ILAHI', command = song5)
d.grid(column=3,row=65)
d.place(x=1000,y=900) 
    
s = tkinter.Button(songs, text = 'KABIRA',command = song6)
s.grid(column=3,row=65)
s.place(x=400,y=900)    
    
    
r = tkinter.Button(songs, text = 'HAAN YAHI RAASTA HAI', command = song7)
r.grid(column=34,row=45)
r.place(x=10,y=90)
    
    
i = tkinter.Button(songs, text = 'KAR HAR MAIDAAN FATEH', command = song8)
i.grid(column=67,row=33)
i.place(x=330,y=220)
    
    
l = tkinter.Button(songs, text = 'ZINDA', command = song9)
l.grid(column=63,row=24)
l.place(x=78,y=90)
    
    
l1 = tkinter.Button(songs, text = 'ZIDDI DIL', command = song10)
l1.grid(column=43,row=65)
l1.place(x=150,y=90)
    
    
y = tkinter.Button(songs, text = 'SADDA HAQ', command = song11)
y.grid(column=78,row=45)
y.place(x=421,y=90)
    
songs.mainloop()