import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image


def food1():
    webbrowser.open_new_tab('https://www.swiggy.com/search?q=hot+milk')

def food2():
    webbrowser.open_new_tab('https://www.frugivore.in/product-details/cherry-imported?gclid=Cj0KCQiA2vjuBRCqARIsAJL5a-K_ZeTex7MFH9BESnNRou8OntK7RwxMYlVvKGruCrh4NiPFyFVbuHsaAimZEALw_wcB')

def food3():
    webbrowser.open_new_tab('https://www.bigbasket.com/pc/foodgrains-oil-masala/dry-fruits/almonds/')

def food4():
    webbrowser.open_new_tab('https://www.bigbasket.com/ss/dark-chocolate/')

def food5():
    webbrowser.open_new_tab('https://www.frugivore.in/product-details/raw-banana')

def food6():
    webbrowser.open_new_tab('https://www.swiggy.com/search?q=oats')

def food7():
    webbrowser.open_new_tab('https://teatrunk.in/products/chamomile-tea?variant=6600765187&currency=INR&cmp_id=1625692718&adg_id=62198179416&kwd=&device=c&gclid=Cj0KCQiA2vjuBRCqARIsAJL5a-LTJMcsXS-ZC8PxFLCdJ-Phkydr55xhvGz8YhA1yaJJnyobNZJMhbIaAs5_EALw_wcB')

def food8():
    webbrowser.open_new_tab('https://www.bigbasket.com/pd/10000560/fresho-kiwi-green-1-pc/')

def food9():
    webbrowser.open_new_tab('https://www.amazon.in/pack-Passion-Flower-Organic-Bleach/dp/B00DLLZZXM')

def food10():
    webbrowser.open_new_tab('https://www.honeybasket.in/?gclid=Cj0KCQiA2vjuBRCqARIsAJL5a-L93kkRFJ5VD3wdZtC8wxeEsuoQ9TWniLbpmfeOa6E-QmBQvVqAtLAaAgc2EALw_wcB')

food = tkinter.Tk()
food.geometry('960x720')
food.configure(bg = 'ivory3')
    
berries_image = PhotoImage(file = 'circle-cropped.png')
bi = berries_image.subsample(5,5)
berries = tkinter.Button(food, text = 'berries',image = bi,compound = TOP, command = food1)
berries.grid(column=0,row=1)
berries.place(x=500,y=10)
    
chicken_image=PhotoImage(file = 'circle-cropped (2).png')
ci = chicken_image.subsample(5,5)
chicken = tkinter.Button(food, text = 'chicken',image = ci, command = food2)
chicken.grid(column = 96, row = 85)
chicken.place(x = 550, y = 70)
    
cnsa = PhotoImage(file = 'circle-cropped (1).png')
cs= cnsa.subsample(5,5)
cns = tkinter.Button(food, text = 'chicken noodle soup',image=cs, command = food3)
cns.grid(column = 18, row = 36)
cns.place(x = 600, y = 140)
    
darkimage = PhotoImage(file = 'circle-cropped (5).png')
ds=darkimage.subsample(5,5)
dark_chocolate = tkinter.Button(food, text = 'Dark Chocolate',image=ds, command = food5)
dark_chocolate.grid(column = 16, row = 13)
dark_chocolate.place(x = 550, y = 210)
  
gy = PhotoImage(file = 'circle-cropped (6).png')
gys=gy.subsample(5,5)
greek_yogurt = tkinter.Button(food, text = 'Greek Yogurt',image=gys, command = food6)
greek_yogurt.grid(column=3,row=65)
greek_yogurt.place(x=500,y=280)
   
gt=PhotoImage(file = 'circle-cropped (3).png')
gts=gt.subsample(5,5)
green_tea = tkinter.Button(food, text = 'Green Tea',image=gts, command = food7)
green_tea.grid(column=78,row=45)
green_tea.place(x=400,y=240)
    
    
pz=PhotoImage(file ='circle-cropped (4).png')
pza=pz.subsample(5,5)
pizza = tkinter.Button(food, text = 'Pizza',image=pza, command  = food9)
pizza.grid(column = 75,row = 22)
pizza.place(x=400,y=120)
'''    
ic=PhotoImage(file = 'icecream.png')
ica=ic.subsample(5,5)
ice_cream = tkinter.Button(food, text = 'Ice Cream',image=ica, command = food10)
ice_cream.grid(column=63,row=24)
ice_cream.place(x=450,y=50)
'''    
food.mainloop()