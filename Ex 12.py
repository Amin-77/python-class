import tkinter
win=tkinter.Tk()
lb1=tkinter.Label(win,text='user')
lb1.pack()
en1=tkinter.Entry(win)
en1.pack()
lb2=tkinter.Label(win,text='password')
lb2.pack()
en2=tkinter.Entry(win)
en2.pack()
user='admin'
password='12345'
def checker():
    if en1.get()==user and en2.get()==password:
        btn.config(fg='green')
    else:
        btn.config(fg='red')
btn=tkinter.Button(win,text='Enter',command=checker)
btn.pack()
str1=tkinter.StringVar()
