# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:57:44 2020
Author: JAIRI IDRISS
---------- MEMORY GAME --------------

@author: hp
"""

#Importing Section

from tkinter import *
import random
import time



#### GLOBAL VARIABLES ######

#data list contains the data in the cards
data = ["电","买","车","爱","鱼","听","气","岁"]
data_length = len(data)


#to check if the game ends, No more available cards
game_end = 0

#dictionary stores buttons(keys) and their texts(values)
dict_cards = {}

#to check how many cards clicked if 2, stop and check similarity
clicked_cards = 0

#fst_ refers to first clicked card
fst_ = ""

#scnd_ refers to second clicked card
scnd_ = ""

#store the moment when the game starts
start = time.time()

#initialize or initiate our root(window)
root = Tk()
root.resizable(False,False)
root.title("Memory Game")

#first frame_

f1 = Frame(root)
f1.pack()

#fonts 
fonts = ['Helvetica', '20', 'bold']

bt1 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt1))
bt1.grid(row=0,column=0,padx=20, pady=40)
dict_cards[bt1] = ""

bt2 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt2))
bt2.grid(row=0,column=1,padx=20, pady=40)
dict_cards[bt2] = ""

bt3 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt3))
bt3.grid(row=0,column=2,padx=20, pady=40)
dict_cards[bt3] = ""

bt4 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt4))
bt4.grid(row=0,column=3,padx=20, pady=40)
dict_cards[bt4] = ""


#second frame_

f2 = Frame(root)
f2.pack()

bt5 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt5))
bt5.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt5] = ""

bt6 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt6))
bt6.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt6] = ""

bt7 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt7))
bt7.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt7] = ""

bt8 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt8))
bt8.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt8] = ""


#third frame_

f3 = Frame(root)
f3.pack()

bt9 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt9))
bt9.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt9] = ""

bt10 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt10))
bt10.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt10] = ""

bt11 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt11))
bt11.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt11] = ""

bt12 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt12))
bt12.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt12] = ""


#forth frame_

f4 = Frame(root)
f4.pack()

bt13 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt13))
bt13.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt13] = ""

bt14 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt14))
bt14.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt14] = ""

bt15 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt15))
bt15.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt15] = ""

bt16 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt16))
bt16.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt16] = ""



######### USED FUNCTIONS #########


#this function to set random data to our cards
def random_text():
    
    #record if the data has occured twice
    occurances = {"电":0,"买":0,"车":0,"爱":0,"鱼":0,"听":0,"气":0,"岁":0}
    
    for bttn in dict_cards:
        
        if len(data) > 0:
            random.shuffle(data)
            x = data[0]
            dict_cards[bttn] = x
            occurances[x] = occurances[x] + 1
        
            if occurances[x] == 2:
                data.remove(x)
        
    
#this function is called when we click a card    
def bttn_clicked(btn):
    global clicked_cards
    global fst_
    global scnd_
    
    
    clicked_cards = clicked_cards + 1
    
    if clicked_cards == 1:
        fst_ = btn
        btn.configure(text=dict_cards[btn],state=DISABLED) 
    
    if  clicked_cards == 2:
        scnd_ = btn
        btn.configure(text=dict_cards[btn],state=DISABLED)
        
        root.after(500,check_same)
        

#this function to check if the two cards are similar
def check_same():
    global clicked_cards
    global fst_
    global scnd_
    global game_end
    global data_length
    
    if scnd_['text'] != fst_['text']:
        fst_.configure(text="",state="normal")
        scnd_.configure(text="",state="normal")
    else:
        game_end = game_end + 1
        

    if game_end == data_length:
        messagebox.showinfo("MEMORY GAME", "You have spent "+str(int(time.time() - start))+" sec!")
        root.destroy()
            
    clicked_cards = 0
            
    
    
        
#calling the function  random_text   
random_text() 

            
#run out window
root.mainloop()


