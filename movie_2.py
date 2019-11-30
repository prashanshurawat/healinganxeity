import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image


def movie1():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/7001900')

def movie2():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70107406')

def movie3():
    webbrowser.open_new_tab('https://www.amazon.com/Kings-Speech-Colin-Firth/dp/B004R36QU')

def movie4():
    webbrowser.open_new_tab('https://www.amazon.com/dp/B000HX6VD')

def movie5():
    webbrowser.open_new_tab('https://www.amazon.com/Kill-Bill-1-Uma-Thurman/dp/B006RXQ8RI')

def movie6():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/60023617')

def movie7():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70087087')

def movie8():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/60020906')

def movie9():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70047320?source=35')

def movie10():
    webbrowser.open_new_tab('https://www.amazon.com/Zindagi-Milegi-Dobara-Hrithik-Roshan/dp/B06WVTDV7Q')

def movie11():
    webbrowser.open_new_tab('https://www.primevideo.com/detail/Chak-De-India/0ST8IWCMUO5NMQM3413WKVMWQS')

def movie12():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/80032364?source=35')

movie = tkinter.Tk()
movie.geometry('1920x1080')
movie.configure(bg = 'CadetBlue1')
frozen = tkinter.Button(movie, text = 'COACH CARTER', command = movie1)
frozen.grid(column = 87, row = 44)
frozen.place(x = 89, y = 996)
    
cacm = tkinter.Button(movie, text = '17 AGAIN', command = movie2)
cacm.grid(column = 96, row = 23)
cacm.place(x = 70, y = 1020)
    
coco = tkinter.Button(movie, text = "THE KING'S SPEECH" , command = movie3)
coco.grid(column = 25, row = 99)
coco.place(x = 59,y = 99)
    
benji = tkinter.Button(movie,text ='SCHOOL OF ROCK', command = movie4)
benji.grid(column = 99,row = 109)
benji.place(x = 109, y = 996)
    
tabhl = tkinter.Button(movie, text = 'KILL BILL', command = movie5)
tabhl.grid(column = 75, row = 180)
tabhl.place(x = 400, y= 300)
    
kissing_booth = tkinter.Button(movie, text = 'JACKASS', command = movie6)
kissing_booth.grid(column = 99, row = 229)
kissing_booth.place(x = 44, y = 19)
  
abmm = tkinter.Button(movie, text = 'TAARE ZAMEEN PAR', command = movie7)
abmm.grid(column = 52, row = 78)
abmm.place(x = 156, y = 989)
    
idiots = tkinter.Button(movie, text = 'LAGAAN', command = movie8)
idiots.grid(column = 445, row = 89)
idiots.place(x = 445, y = 1005)
    
rajma_chawal = tkinter.Button(movie, text = 'RANG DE BASANTI', command = movie9)
rajma_chawal.grid(column = 78, row = 8)
rajma_chawal.place(x = 341, y = 363)
    
catwalk = tkinter.Button(movie, text = 'ZINDAGI NA MILEGI DOOBARA', command = movie10)
catwalk.grid(column = 457, row = 998)
catwalk.place(x = 85, y = 34)
    
someone_great = tkinter.Button(movie, text = 'CHAK DE INDIA', command = movie11)
someone_great.grid(column = 225, row = 365)
someone_great.place(x = 663, y = 85)
    
set_it_up = tkinter.Button(movie, text = 'PUNJAB 1984', command = movie12)
set_it_up.grid(column = 115, row = 285)
set_it_up.place(x = 400, y = 400)
    
movie.mainloop()

