from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import datetime

#建立主視窗
root=Tk()
#設定主視窗大小為1600x800,並從座標(x,y)=(0,0)的位置建立網頁
root.geometry("1600x800+0+0")
#設定主視窗名稱
root.title("約時間神器")

Info=Label(font=('BiauKai',50,'bold'),text='讓約時間不再是團體報告的夢魘')
Info.grid(row=0,column=0)
Info.pack(side='top')

now=datetime.datetime.now()

style = ttk.Style(root)
style.theme_use('clam')
call=Calendar(root,font="Arial 14",background="white", disabledbackground="white", bordercolor="white", 
               headersbackground="white", normalbackground="white",foreground='black', 
               normalforeground='black', headersforeground='black',selectmode='day',year=now.year,month=now.month,day=now.day)
a='0'

def grab_date():
        global a
        text=call.get_date()
        print(text)
        day=text[2]
        print(text[2])
        month=text[0]
        print(text[0])
        a='你選擇 %s 月 %s日'%(month,day)
        my_label.config(text=a)

        

        
call.pack(pady=20,side='left')
my_button=Button(root,text="Confirm",command=grab_date)
my_button.pack(pady=20,side='left')

my_label=Label(root,text="")
my_label.pack(pady=20,side='right')
               
root.mainloop()

