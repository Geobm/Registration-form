from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime

init = Tk()
init.geometry('500x500')
init.title("Nanotechnology Lab Registration")
#init.configure(background = 'white')


Username = StringVar()
area = StringVar()
name = StringVar()
var1 = IntVar()
var2 = IntVar()
admin = StringVar()

def database():
   username = Username.get()
   Name = name.get()
   sector = area.get()
   prog = var1.get()
   if (username == '' or Name == '' or sector == ''):
      messagebox.showinfo("!", "Empty value\nTry again")   
   else : 
      time = datetime.datetime.now()
      conn = sqlite3.connect('Nano.db')
      with conn:
         cursor=conn.cursor()
      cursor.execute('CREATE TABLE IF NOT EXISTS Student (ID TEXT,Name TEXT,Area TEXT,Programs INT,Fecha TEXT)')
      cursor.execute('INSERT INTO Student (ID,Name,Area,Programs,Fecha) VALUES(?,?,?,?,?)',(username,Name,sector,prog,time))
      conn.commit()
      messagebox.showinfo("OK", "Registration\n Succesfully")
      exit()

label_0 = Label(init, text="Nanotechnology \nLab Registration",width=20,font=("bold", 20))
label_0.place(x=90,y=34)


label_1 = Label(init, text="ID: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(init,textvar=Username)
entry_1.place(x=240,y=130)

label_2 = Label(init, text="Name(s):",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(init,textvar=name)
entry_2.place(x=240,y=180)


label_4 = Label(init, text="Section: ",width=20,font=("bold", 10))
label_4.place(x=80,y=250)

list1 = ['Undergraduate','Postgraduate','Other'];

droplist=OptionMenu(init,area, *list1)
droplist.config(width=15)
area.set('Select your area:') 
droplist.place(x=240,y=250)

label_4 = Label(init, text="Usage: ",width=20,font=("bold", 10))
label_4.place(x=85,y=330)

Checkbutton(init, text="IR spectroscopy", variable=var1).place(x=235,y=330)
Checkbutton(init, text="Other programs", variable=var2).place(x=235,y=350)

Button(init, text='Submit',width=20,bg='grey',fg='white',command=database).place(bordermode = OUTSIDE, x=180, y=400)

init.mainloop()

