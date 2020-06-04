import numpy
from tkinter import messagebox
import tkinter as tk
import random
win=tk.Tk()
win.geometry('225x200')
win.resizable(width=False, height=False)
win.config(bg='thistle1')
i=tk.IntVar()
x=20
y=15
s=0
str4=''
list_f=list()
set3=set()
def starter():
    lb1=tk.Label(win,text='Please select the desired difficulty',bg='thistle1')
    lb1.place(relx=0,rely=0)
    str1=tk.StringVar()
    rbtn1=tk.Radiobutton(win,text='easy',variable=i,value=1,bg='thistle1')
    rbtn2=tk.Radiobutton(win,text='medium',variable=i,value=2,bg='thistle1')
    rbtn3=tk.Radiobutton(win,text='hard',variable=i,value=3,bg='thistle1')
    rbtn1.place(relx=0.5,rely=0.2,anchor='center')
    rbtn2.place(relx=0.5,rely=0.4,anchor='center')
    rbtn3.place(relx=0.5,rely=0.6,anchor='center')
    btn1=tk.Button(win,text='START',command=game)
    btn1.place(relx=0.4,rely=0.8)
def game():
    win2=tk.Tk()
    win2.geometry('500x350')
    win2.resizable(width=False, height=False)
    win2.config(bg='turquoise')
    list_easy=['rock','sand','book','bed','apply']
    list_medium=['pillow','building','laptop','advice','appeal','camera']
    list_hard=['unnecessary','punctuality','negligable','disabilitating']
    if i.get()==1:
        str1=random.choice(list_easy)
    if i.get()==2:
        str1=random.choice(list_medium)
    if i.get()==3:
        str1=random.choice(list_hard)
    print(str1)
    lb2=tk.Label(win2,text='Lives: ',background='turquoise')
    lb2.grid(row=0,column=0)
    lb3=tk.Label(win2,text='Your word so far: ',background='turquoise')
    lb3.grid(row=1,column=0)
    lb6=tk.Label(win2,text='The incorrect\n letters: ',background='turquoise')
    lb6.grid(row=2,column=0)
    cn=tk.Canvas(win2,width=200,height=30,background='turquoise',highlightthickness=0)
    cn.grid(row=0,column=1)
    cn2=tk.Canvas(win2,width=300,height=50,background='turquoise',highlightthickness=0)
    cn2.grid(row=1,column=1)
    j=4
    global x,y,s,list_f,str4,set3
    
    while j>0:
        j-=1
        cn.create_oval(x-10,y-10,x+10,y+10,fill='black')
        x+=30
    x-=30
    en=tk.Entry(win2)
    en.place(relx=0.5,y=250,anchor='center')
    lb3=tk.Label(win2,text='Please enter just one letter!',background='turquoise')
    lb3.place(relx=0.5,y=225,anchor='center')
    list1=list(str1)
    set1=set(str1)
    set2=set()
    len_1=len(str1)
    c_len=0
    str3=''
    while c_len<len_1:
        str3+='_ '
        c_len+=1
    cn2.create_text(10,15,anchor='nw',text=str3,font='Courier')
    
        
    def l_checker():
        global x,y,s,list_f,str4,set3
        t=False
        g=False
        if en.get().lower() not in list1:
            if en.get().lower() not in set3:
                set3.add(en.get().lower())
                cn.create_oval(x-10,y-10,x+10,y+10,fill='white')
                x-=30
                s+=1
                if len(en.get().lower())==1:
                    str4+=en.get().lower()
                if len(en.get())>1:
                    o=messagebox.showwarning('In correct letter',"You've entered more than one letter!")
                    x+=30
                    cn.create_oval(x-10,y-10,x+10,y+10,fill='black')
                    s-=1
                if en.get().lower()>'z' or en.get().lower()<'a':
                    o=messagebox.showwarning('Invalid letter',"You've entered an invalid letter!")
                    x+=30
                    cn.create_oval(x-10,y-10,x+10,y+10,fill='black')
                    s-=1
            else:
                o=messagebox.showwarning('In correct letter',"You've already tried that letter!")
            lb7=tk.Label(win2,text=str4,background='turquoise')
            lb7.place(relx=0.3,rely=0.27,anchor='nw')
        else:
            list_f.append(en.get())
            c_len=0
            str3=''
            
            set2.add(en.get().lower())
            while c_len<len_1:
                if en.get().lower() not in list1[c_len]:
                    str3+='  '
                else:
                    
                    str3+=en.get().lower()
                    str3+=' '
                    cn2.create_text(10,15,anchor='nw',text=str3,font='Courier')
                c_len+=1
            if set1==set2:
                s=0
                x=20
                str4=''
                g=messagebox.askyesno('Congratulations!','You Won! do you want to restart?')
                set3=set()
                win2.destroy()
                if g!=True:
                    win.destroy()
        
        if g:
            starter()
        if s==4:
            str4=''
            s=0
            x=20
            win2.destroy()
            t=messagebox.askyesno('Restart','You lost! do you want to restart?')
            set3=set()
            if t!=True:
                win.destroy()
        if t:
            set2.clear()
            starter()
    btn2=tk.Button(win2,text='Enter',command=l_checker)
    btn2.place(relx=0.5,y=280,anchor='center')
starter()

