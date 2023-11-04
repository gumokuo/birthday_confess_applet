#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 06:57:43 2020

@author: ken
"""

import tkinter as tk
import tkinter.messagebox

def closeWindow():
    tk.messagebox.showinfo(title="警告",message = "不許關閉，好好回答")
    return

def Love():
    love = tk.Toplevel(window)
    love.geometry("900x60+300+360")
    love.title("來自Ken的Message")
    label = tk.Label(love,text="Happy Birthday!!在這特別的日子裡，我沒特別準備什麼，禮物就是在生日這天你向Ken說的任何事，他都會說『Yes』哦~~",font =("微軟雅黑",15))
    label.pack()
    btn = tk.Button(love,text="確定",width=10 , height=1,command=close_all)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW",closelove)

def closelove():
    return

#destroy all win
def close_all():
    window.destroy()

def closenolove():
    #messagebox.showinfo("再考慮一下","再考慮一下唄")
    #return
    disLove()

def disLove():
    no_love = tk.Toplevel(window)
    no_love.geometry("420x60+300+360")
    no_love.title("oh~~No~~")
    label =  tk.Label(no_love,text = "別這樣，再考慮一下，或許會有意想不到的驚喜哦~~",font = ("微軟雅黑",15))
    label.pack()
    btn = tk.Button(no_love,text = "好的",width = 10 , height = 1,command = no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW",closenolove)

window=tk.Tk()
window.title("Ken的告白")
window.geometry("315x405")

#triggered by closing win
window.protocol("WM_DELETE_WINDOW",closeWindow)

label=tk.Label(window, text = "Hey,haruka姐姐", font=("微軟雅黑",12), fg="black")
label.grid(row=0,column=0)

label_1=tk.Label(window,text = "你好漂亮，可以和我交往嗎？",font=("微軟雅黑",12))
label_1.grid(row=1,column=1,sticky=tk.E)

#set photo
photo=tk.PhotoImage(file=r"/Users/kenkuo/Downloads/ayasei.png")
imageLable=tk.Label(window,image=photo)
imageLable.grid(row=2,column=0,columnspan=2)

btn=tk.Button(window,text="可以",command=Love)
btn.grid(row=3,column=0,sticky=tk.W)

btn1=tk.Button(window,text="不可以",command=disLove)
btn1.grid(row=3,column=1,sticky=tk.E)
#display win
window .mainloop()