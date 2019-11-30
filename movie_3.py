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
    webbrowser.open_new_tab('https://www.amazon.com/dp/B0026SB1XO')

def movie2():
    webbrowser.open_new_tab('https://www.amazon.com/Last-Holiday-LL-Cool-J/dp/B00BR3NXKS')

def movie3():
    webbrowser.open_new_tab('https://www.primevideo.com/detail/Before-Sunrise/0NU6XEYK4WK7T4L6O704WEBV7S?ref_=dvm_pds_gen_in_as_s_gt_dsaallwebpages')

def movie4():
    webbrowser.open_new_tab('https://www.amazon.com/Finding-Theatrical-Version-Ellen-DeGeneres/dp/B01H2HGTO4')

def movie5():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/60031747')

def movie6():
    webbrowser.open_new_tab('https://www.primevideo.com/detail/0J7ZD4X51ZHWK330TL9WH5NMHU/?ref_=dvm_pds_gen_in_as_s_gt_38426|c_198967413020_m_b10421bM-dc_s_')

def movie7():
    webbrowser.open_new_tab('https://www.amazon.com/500-Days-Summer-Joseph-Gordon-Levitt/dp/B00BZBWXZS')

def movie8():
    webbrowser.open_new_tab('https://www.amazon.com/High-School-Musical-Zac-Efron/dp/B00BZC1P38')

def movie9():
    webbrowser.open_new_tab('https://www.amazon.com/In-Her-Shoes-Cameron-Diaz/dp/B001EQ04BY')

def movie10():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70243574?source=35')

def movie11():
    webbrowser.open_new_tab('https://www.amazon.com/Snow-Day-Chris-Elliott/dp/B001MFPT94/ref=redir_mobile_desktop?_encoding=UTF8&%2AVersion%2A=1&%2Aentries%2A=0')

def movie12():
    webbrowser.open_new_tab('https://www.amazon.com/Hum-Dil-Chuke-Sanam-Aishwarya/dp/B078GZKDS1')

def movie13():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70089214?source=35')

def movie14():
    webbrowser.open_new_tab('https://www.netflix.com/in/title/70087087?source=35')

movie = tkinter.Tk()
movie.geometry('1920x1080')
movie.configure(bg = 'CadetBlue1')

fr=PhotoImage(file='clueless.png')
frz=fr.subsample(5,5)
frozen = tkinter.Button(movie, text = 'COACH CARTER',image = frz, command = movie1)
frozen.grid(column = 87, row = 44)
frozen.place(x = 709, y = 506)
    
sr=PhotoImage(file='last_holiday.png')
src=sr.subsample(2,2)
cacm = tkinter.Button(movie, text = '17 AGAIN',image = src, command = movie2)
cacm.grid(column = 96, row = 23)
cacm.place(x = 50, y = 120)
    
Bf=PhotoImage(file='before sunrise.png')
bff=Bf.subsample(5,5)
coco = tkinter.Button(movie, text = "THE KING'S SPEECH" ,image = bff, command = movie3)
coco.grid(column = 25, row = 99)
coco.place(x = 559,y = 999)
    
fd=PhotoImage(file='finding dory.png')
fdd=fd.subsample(5,5)
benji = tkinter.Button(movie,text ='SCHOOL OF ROCK',image = fdd, command = movie4)
benji.grid(column = 99,row = 109)
benji.place(x = 609, y = 326)
    
an=PhotoImage(file='annie.png')
ann=an.subsample(2,2)
tabhl = tkinter.Button(movie, text = 'KILL BILL',image = ann, command = movie5)
tabhl.grid(column = 75, row = 180)
tabhl.place(x = 800, y = 600)
    
ks=PhotoImage(file='twilight.png')
kss=ks.subsample(5,5)
kissing_booth = tkinter.Button(movie, text = 'JACKASS',image = kss, command = movie6)
kissing_booth.grid(column = 99, row = 229)
kissing_booth.place(x = 44, y = 19)
  
hg=PhotoImage(file='high school musical.png')
hgg=hg.subsample(1,1)
idiots = tkinter.Button(movie, text = 'LAGAAN',image = hgg, command = movie8)
idiots.grid(column = 445, row = 89)
idiots.place(x = 215, y = 105)
    
sg=PhotoImage(file='safe heaven.png')
sgg=sg.subsample(2,2)    
catwalk = tkinter.Button(movie, text = 'ZINDAGI NA MILEGI DOOBARA',image = sgg, command = movie10)
catwalk.grid(column = 457, row = 998)
catwalk.place(x = 58, y = 704)
    
sd=PhotoImage(file='snow day.png')
sdd=sd.subsample(5,5)
someone_great = tkinter.Button(movie, text = 'CHAK DE INDIA',image = sdd, command = movie11)
someone_great.grid(column = 225, row = 365)
someone_great.place(x = 606, y = 85)
    
hdd=PhotoImage(file='hum dil de chuke snama.png')
hddd=hdd.subsample(2,2)
set_it_up = tkinter.Button(movie, text = 'PUNJAB 1984',image = hddd, command = movie12)
set_it_up.grid(column = 115, row = 285)
set_it_up.place(x = 400, y = 65)

movie.mainloop()

