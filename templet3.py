import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image
import os
import sys

def music():
    os.system('python songs_3.py')

def movies():
    os.system('python movie_3.py')

def foods(): 
    os.system('python food_#.py')
def hello1():
    webbrowser.open_new_tab('https://www.miniclip.com/games/en/')

def hello4():    
    messagebox.showinfo('SONG',"would you like to listen songs ")

def sleep():    
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=w6sbrmcrSuo')

def drawing():    
    webbrowser.open_new_tab('https://www.autodraw.com/')

def art():    
    webbrowser.open_new_tab('https://m.thecolor.com/Coloring/4-by-4-coloring-page.aspx')

def hello8():    
    messagebox.showinfo('CONTACT',"would you like to contact somebody")

def min5():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=zwSRF3QkG7Q')

def min10():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=4oTfGFUjutw')

def min15():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=UBnfm4s7CRA')


    
    #temp1.configure(bg='pink')
canvas = tkinter.Canvas(width=600, height=400, bg='black')
canvas.pack()
gif1 = tkinter.PhotoImage(file='1 (1).png')
w = gif1.width()
h = gif1.height()

game_image = PhotoImage(file = 'ngame.png')
gi = game_image.subsample(5,5)
a = tkinter.Button(text='GAME',image = gi,compound = TOP, command = hello1)
#a.grid(column=0,row=1)
a.configure(width = 90, height = 90)
#a.place(x=380,y=241)
a_window = canvas.create_window(380, 40, window = a)

food_image = PhotoImage(file = 'nfood.png')
pi = food_image.subsample(5,5)
b = tkinter.Button(text='FOOD',image=pi,compound=TOP,command = foods)
#b.grid(column=1,row=2)
#b.place(x=550,y=60)
b.configure(width = 90, height = 90)
b_window = canvas.create_window(331, 221, window = b)

movie_image = PhotoImage(file = 'nmovies.png')
mi = movie_image.subsample(5,5)
c = tkinter.Button(text='MOVIE',image=mi,compound=TOP,command = movies)
#c.grid(column=2,row=3)
#c.place(x=600,y=90)
c.configure(width = 90, height = 90)
c_window = canvas.create_window(540, 210, window = c)

music_image = PhotoImage(file = 'nmusic.png')
mi1 = music_image.subsample(5,5)
d = tkinter.Button(text='SONG',image = mi1,compound = TOP,command = music)
#d.grid(column=3,row=4)
#d.place(x=550,y=120)
d.configure(width = 90, height = 90)
d_window = canvas.create_window(460, 295, window = d)

sleep_image = PhotoImage(file = 'nsleep.png') 
si = sleep_image.subsample(5,5)   
e = tkinter.Button(text='SLEEP',image = si, compound = TOP,command = sleep)
#e.grid(column=4,row=3)
#e.place(x=500,y=150)
e.configure(width = 90, height = 90)
e_window = canvas.create_window(500, 125, window = e)

exercise_image = PhotoImage(file = 'nworkout.png')
ei = exercise_image.subsample(5,5)    
f = tkinter.Button(text='EXERCISE',image = ei,compound = TOP,command = min10)
#f.grid(column=3,row=2)
#f.place(x=400,y=120)
f.configure(width = 90, height = 90)
f_window = canvas.create_window(300, 125, window = f)


canvas.create_image(305,200,image=gif1)
 
tkinter.mainloop()
