from tkinter import *
import sqlite3

init = Tk()
init.geometry('500x500')
init.title("Nanotechnology Lab Registration")


Username = StringVar()
area = StringVar()
password = StringVar()
var1 = IntVar()
var2 = IntVar()

def clear():

   database().destroy()   


def database():
   username = Username.get()
   passw = password.get()
   sector = area.get()
   prog = var1.get()
   conn = sqlite3.connect('Nanotechnology.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Username TEXT,Password TEXT,Area TEXT,Programs INT)')
   cursor.execute('INSERT INTO Student (Username,Password,Area,Programs) VALUES(?,?,?,?)',(username,passw,sector,prog))
   conn.commit()

   sucess = Tk()
   sucess.geometry('180x200')
   sucess.title("Confirm?")
   Label_1 = Label(sucess, text = "Successful\n registration", fg = "green" ,font = ("calibri", 11))
   Label_1.place(x=50,y=65)
   Button(sucess, text='ok',heigh = 1, width=2,bg='grey',fg='white').place(height=30, width=50,x=50,y=120)
   

label_0 = Label(init, text="Nanotechnology \nLab Registration",width=20,font=("bold", 20))
label_0.place(x=90,y=34)


label_1 = Label(init, text="Username",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(init,textvar=Username)
entry_1.place(x=240,y=130)

label_2 = Label(init, text="Password",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(init,textvar=password)
entry_2.place(x=240,y=180)
entry_2.config(show="*")


label_4 = Label(init, text="Section ",width=20,font=("bold", 10))
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

Button(init, text='Submit',width=20,bg='grey',fg='white',command=database).place(bordermode = OUTSIDE, x=180, y=380)
#Button(init, text'Clear'width = 10, bg='grey', command = clear).place(x=250,380 y= )
init.mainloop()

