import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image
import os
import sys

def UI():
    os.system('python UI.py')
canvas = tkinter.Canvas(width=1587, height=1245, bg='black')
canvas.pack()
gif1 = tkinter.PhotoImage(file='Hey you!.png')
w = gif1.width()
h = gif1.height()
a = tkinter.Button(text='YES', command = UI,bg='lightpink')
#a.grid(column=0,row=1)
a.configure(width = 15, height = 10)
#a.place(x=380,y=241)
a_window = canvas.create_window(380, 40, window = a)
canvas.create_image(758,624,image=gif1)
 
tkinter.mainloop()
