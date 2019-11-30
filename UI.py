import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image
import os
import sys

#pygame.mixer.music.load("")
'''top = tkinter.Tk()
top.geometry("1920x1080")
top.configure(bg = 'DarkseaGreen1')'''
#myFont = font.Font(family = 'Arial', size = 17, weight = 'normal')

def templet1():
    os.system('python templet1.py')

def templet2():
    os.system('python templet2.py')

def templet3():
    os.system('python templet3.py')

def templet4():
    os.system('python templet4.py')

text1 = '''I feel little low, maybe lonely 
           ,IDK I am sad'''    
text2 = '''I lack energy and feel low,
           though i have a work to do'''
text3 = '''I feel so exhausted,
           I need a break,
        and maybe a nap too'''
text4 = '''I an just ANXIOUS,
           IDK why!!'''

canvas = tkinter.Canvas(width=1310, height=736, bg='black')
canvas.pack()
gif1 = tkinter.PhotoImage(file='alexey-marchenko-I_O-v19bnJQ-unsplash.png')
w = gif1.width()
h = gif1.height()

te1 = PhotoImage(file = 't1finallogo.png')
te = te1.subsample(3,3)
t1 = tkinter.Button(text = text1,image = te,compound =TOP, command = templet1, bg = 'lightpink')
t1.config(height = 230,width = 200)
#t1.grid(column = 10, row = 10)
#t1.place(x = 200,y = 150)
#t1['font'] = myFont
#t1.configure(width = 20, height = 6)
t1_window = canvas.create_window(200, 150, window = t1)

te2 = PhotoImage(file = 't2finallogo.png')
tr = te2.subsample(3,3)
t2 = tkinter.Button(text = text2,image = tr,compound = TOP, command = templet2, bg = 'yellow')
t2.config(height=200,width=200)
#t2.grid(column = 40,row = 20)
#t2.place(x = 800,y = 250)
#t2['font'] = myFont
t2_window = canvas.create_window(800, 250, window = t2)

te3 = PhotoImage(file = 't3finallogo.png')
ty = te3.subsample(3,3)
t3 = tkinter.Button(text = text3,image = ty, compound = TOP, command = templet3 , bg = 'lightblue')
t3.config(height = 200, width = 200)
#t3.grid(column = 10, row = 40)
#t3.place(x = 200,y = 450)
#t3['font'] = myFont
t3_windows = canvas.create_window(200, 450, window = t3)

'''te4 = PhotoImage(file = 't4finallogo.png')
tu = te4.subsample(3,3)
t4 = tkinter.Button(text=text4,image = tu,compound = TOP,command=templet4,bg='grey40')
t4.config(height=200,width=200)
#t4.grid(column = 40,row = 60)
#t4.place(x = 800, y = 550)
#t4['font'] = myFont
t4_windows = canvas.create_window(800, 550, window = t4)
'''
canvas.create_image(656.125, 370, image=gif1)
mainloop()