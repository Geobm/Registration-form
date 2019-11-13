from tkinter import *
import sqlite3
from time import sleep
import datetime


root = Tk()
root.geometry('500x500')
root.title("Nanotechnology Lab Registration")


Username = StringVar()
area = StringVar()
password = StringVar()
var1 = IntVar()
var2 = IntVar()
time = 0

#def delete_user():


def database():
      username = Username.get()
      passw = password.get()
      if (passw == 'abc'):
         print("ok")
      else :
         sector = area.get()
         prog = var1.get()
         time = datetime.datetime.now()
         conn = sqlite3.connect('Nanotechnology.db')
         with conn:
            cursor=conn.cursor()
         cursor.execute('CREATE TABLE IF NOT EXISTS Student (Username TEXT,Password TEXT,Area TEXT,Programs INT,Fecha TEXT)')
         cursor.execute('INSERT INTO Student (Username,Password,Area,Programs,Fecha) VALUES(?,?,?,?,?)',(username,passw,sector,prog,time))
         conn.commit()
         Label(root, text= "Succesful Registration", fg="green", font =("bold",12)).place(x=180, y=450)
         sleep(3)
         root.destroy() 
         


label_0 = Label(root, text="Nanotechnology \nLab Registration",width=20,font=("bold", 20))
label_0.place(x=90,y=34)


label_1 = Label(root, text="ID: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Username)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=password)
entry_2.place(x=240,y=180)
entry_2.config(show="*")


label_4 = Label(root, text="Section ",width=20,font=("bold", 10))
label_4.place(x=80,y=250)

list1 = ['Undergraduate','Postgraduate','Other'];

droplist=OptionMenu(root,area, *list1)
droplist.config(width=15)
area.set('Select your area:') 
droplist.place(x=240,y=250)

label_4 = Label(root, text="Usage: ",width=20,font=("bold", 10))
label_4.place(x=85,y=330)

Checkbutton(root, text="IR spectroscopy", variable=var1).place(x=235,y=330)
Checkbutton(root, text="Other programs", variable=var2).place(x=235,y=350)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
#Button(root, text = 'Clear', width=10, bg='grey', fg='white', command=takes_input).place(x=180,y=420)
root.mainloop()
