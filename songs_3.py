import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image
def song1():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=7wfYIMyS_dI')

def song2():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=dVNdTXEJv1A')

def song3():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=T5xcnjAG8pE')

def song4():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=W1tzURKYFNs')

def song5():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=u7K72X4eos')

def song6():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=COz9lDCFHjw')

def song7():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=kdgN86GTttU')

def song8():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=gS1c3-iKwfk')

def song9():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=sK7riqg2mr4')

def song10():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=DK_UsATwoxI')

def song11():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=2kgEc6oH9J0')

def song12():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=HnLtNrvfZTU')

def song13():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=E8rpY2FwKkY')

songs = tkinter.Tk()
songs.geometry("1920x1080")
songs.configure(bg = 'khaki1')
    
    
ill=PhotoImage(file='circle-cropped (7).png')
ilh=ill.subsample(5,5)
ilahi = tkinter.Button(songs, text = 'ilahi',image=ilh, command = song1)
ilahi.grid(column=0,row=1)
ilahi.place(x=500,y=10)
    
    
bph=PhotoImage(file='circle-cropped (17).png')
bphl=bph.subsample(5,5)
badal_paon_hai = tkinter.Button(songs, text = 'badal paon hai',image=bphl, command = song2)
badal_paon_hai.grid(column=1,row=2)
badal_paon_hai.place(x=300,y=100) 
    
    
ash=PhotoImage(file='circle-cropped (19).png')
asy=ash.subsample(5,5)
ashayein = tkinter.Button(songs, text = 'ashayein',image=asy, command = song3)
ashayein.grid(column=6,row=15)
ashayein.place(x=600,y=150) 
    
    
pg=PhotoImage(file='circle-cropped (11).png')
pgd=pg.subsample(5,5)
patakha_guddi = tkinter.Button(songs, text = 'patakha guddi',image=pgd, command = song4)
patakha_guddi.grid(column=10,row=9)
patakha_guddi.place(x=550,y=100) 
    
    
aju=PhotoImage(file='circle-cropped (20).png')
ajm=aju.subsample(5,5)
aaj_mai_uuper = tkinter.Button(songs, text = 'aaj mai upper',image=ajm, command = song5)
aaj_mai_uuper.grid(column=3,row=65)
aaj_mai_uuper.place(x=1000,y=900) 
  
    
sc=PhotoImage(file='circle-cropped (13).png')
sch=sc.subsample(5,5)
soch = tkinter.Button(songs, text = 'soch',image=sch,command = song6)
soch.grid(column=3,row=65)
soch.place(x=400,y=900)    
    
    
rk=PhotoImage(file='circle-cropped (12).png')
rkh=rk.subsample(5,5)
rukh = tkinter.Button(songs, text = 'rukh',image=rkh, command = song7)
rukh.grid(column=34,row=45)
rukh.place(x=10,y=90)
    
    
igt=PhotoImage(file='circle-cropped (15).png')
igtt=igt.subsample(5,5)
i_got_you = tkinter.Button(songs, text = 'i got you',image=igtt, command = song8)
i_got_you.grid(column=67,row=33)
i_got_you.place(x=330,y=220)
    
    
lhg=PhotoImage(file='circle-cropped (13).png')
lhgt=lhg.subsample(5,5)
let_her_go = tkinter.Button(songs, text = 'let her go',image=lhgt, command = song9)
let_her_go.grid(column=63,row=24)
let_her_go.place(x=78,y=90)
    
    
ls=PhotoImage(file='circle-cropped (21).png')
lsy=ls.subsample(5,5)
love_story = tkinter.Button(songs, text = 'love story',image=lsy, command = song10)
love_story.grid(column=43,row=65)
love_story.place(x=150,y=90)
    
    
yb=PhotoImage(file='circle-cropped (13).png')
ybm=yb.subsample(5,5)
you_belong_with_me = tkinter.Button(songs, text = 'you belong with me',image=ybm, command = song11)
you_belong_with_me.grid(column=78,row=45)
you_belong_with_me.place(x=421,y=90)
    
    
nb=PhotoImage(file='circle-cropped (10).png')
nmb=nb.subsample(5,5)
numb = tkinter.Button(songs, text = 'numb',image=nmb, command = song12)
numb.grid(column = 75,row = 22)
numb.place(x = 54,y = 22)
    
    
cs=PhotoImage(file='circle-cropped (13).png')
cst=cs.subsample(5,5)
counting_stars = tkinter.Button(songs, text = 'counting stars',image=cst, command = song13)
counting_stars.grid(column=3,row=65)
counting_stars.place(x=100,y=200)

'''awk=PhotoImage(file='circle-cropped (18).png')
alwk=awk.subsample(5,5)
all_we_know = tkinter.Button(songs, text = 'all we know',image=alwk,command = song14)
all_we_know.grid(column=36,row=65)
all_we_know.place(x=140,y=400)'''
    
songs.mainloop()


