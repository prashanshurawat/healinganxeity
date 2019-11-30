import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image
import os
import sys


def movie1():
    webbrowser.open_new_tab('https://www.amazon.com/Frozen-Plus-Bonus-Features-Kristen/dp/B00HV2KT06')

def movie2():
    webbrowser.open_new_tab('https://www.amazon.com/Cloudy-With-Chance-Of-Meatballs/dp/B00304E5NG')

def movie3():
    webbrowser.open_new_tab('https://www.nowtv.com/watch/coco-2017/A5EK6azdkxe1NFdrMgsQQ')

def movie4():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80204923?source=35')

def movie5():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80203147?source=35')

def movie6():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80143556')

def movie7():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80202874?source=35')

def movie8():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70121522?source=35 ')

def movie9():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/81018377?source=35')

def movie10():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/81005561?source=35')

def movie11():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80202920?source=35')

def movie12():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80184100?source=35')

def music():
    os.system('python music_1.py')
    

movie = tkinter.Tk()
movie.geometry('1920x1080')
movie.configure(bg = 'CadetBlue1')



frozen = tkinter.Button(movie, text = 'frozen', command = movie1)
frozen.grid(column = 87, row = 44)
frozen.place(x = 889, y = 996)
    
cacm = tkinter.Button(movie, text = 'cloudy and the chance of meatball', command = movie2)
cacm.grid(column = 96, row = 23)
cacm.place(x = 470, y = 120)
    
coco = tkinter.Button(movie, text = 'coco' , command = movie3)
coco.grid(column = 25, row = 99)
coco.place(x = 505,y = 99)
   
benji = tkinter.Button(movie,text ='benji', command = movie4)
benji.grid(column = 99,row = 109)
benji.place(x = 69, y = 96)
    
tabhl = tkinter.Button(movie, text = 'to all the boys i have loved', command = movie5)
tabhl.grid(column = 75, row = 180)
tabhl.place(x = 82, y= 80)
    
kissing_booth = tkinter.Button(movie, text = 'kissing booth', command = movie6)
kissing_booth.grid(column = 99, row = 229)
kissing_booth.place(x = 104, y = 19)
    
abmm = tkinter.Button(movie, text = 'always be my maybe', command = movie7)
abmm.grid(column = 52, row = 78)
abmm.place(x = 421, y = 9)
    
idiots = tkinter.Button(movie, text = '3 idiots', command = movie8)
idiots.grid(column = 445, row = 89)
idiots.place(x = 405, y = 105)
    
rajma_chawal = tkinter.Button(movie, text = 'Rajma Chawal', command = movie9)
rajma_chawal.grid(column = 78, row = 558)
rajma_chawal.place(x = 201, y = 301)
  
catwalk = tkinter.Button(movie, text = 'catwalk : tales from the cat show circuit', command = movie10)
catwalk.grid(column = 457, row = 998)
catwalk.place(x = 85, y = 754)
    
someone_great = tkinter.Button(movie, text = ' someone great', command = movie11)
someone_great.grid(column = 225, row = 365)
someone_great.place(x = 663, y = 785)
    
set_it_up = tkinter.Button(movie, text = 'set it up', command = movie12)
set_it_up.grid(column = 115, row = 285)
set_it_up.place(x = 900, y = 800)
    
movie.mainloop()
