import tkinter 
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import *
import tkinter.font as font
from PIL import ImageTk,Image

def food1():
    webbrowser.open_new_tab("https://www.zomato.com/ncr/order?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Delhi&gclid=CjwKCAiAh5_uBRA5EiwASW3IagXCwV-vzarXWL-wkefSS4CLeaPlS_eLB1iQhaHWOQBfeyx6mCCu5RoCkX8QAvD_BwE")

def food2():
    webbrowser.open_new_tab("https://www.bigbasket.com/pd/40018540/very-berry-fruits-strawberries-150-g-pouch/?z=MzE0OTkyNTYwOA&utm_source=google&utm_medium=cpc&utm_campaign=Chennai-PLA/&gclid=CjwKCAiAlO7uBRANEiwA_vXQ-2Fzx_gK30FX0VaG7valwlXAwbFOXTW8U-QJhSfQEGlSTFuQvpucaRoCiOEQAvD_BwE")

def food3():
    webbrowser.open_new_tab("https://www.swiggy.com/search?q=chicken")

def food4():
    webbrowser.open_new_tab("https://www.swiggy.com/search?q=chicken+noodle+soup")

def food5():
    webbrowser.open_new_tab("https://www.bigbasket.com/pc/snacks-branded-foods/chocolates-candies/")

def food6():
    webbrowser.open_new_tab("https://www.bigbasket.com/pc/gourmet-world-food/dairy-cheese/flavoured-greek-yogurt/?utm_source=google&utm_medium=cpc&utm_campaign=Dynamic-DSA-Bangalore-PC&gclid=CjwKCAiAlO7uBRANEiwA_vXQ-zQX3l99RAVQtkEaYAvTxOl4cGiGo-jqV6JwpTotJWXdrKv_qfPeBBoCgzEQAvD_BwE")

def food7():
    webbrowser.open_new_tab("https://www.bigbasket.com/pc/beverages/tea/green-tea/")

def food8():
    webbrowser.open_new_tab("https://www.swiggy.com/search?q=salmon")

def food9():
    webbrowser.open_new_tab('https://www.dominos.co.in/menu/veg-pizzas')

def food10():
    webbrowser.open_new_tab('https://www.swiggy.com/restaurants/natural-ice-cream-jmd-kohinoor-mall-greater-kailash-2-delhi-27798')


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
