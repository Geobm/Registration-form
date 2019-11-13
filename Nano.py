from tkinter import *
from tkinter import messagebox
import sqlite3
from time import sleep
import datetime


def database():
	username = Username.get()
	passw = password.get()
 	sector = area.get()
 	prog = var1.get()
	time = datetime.datetime.now()
	conn = sqlite3.connect('Nanotechnology.db')
	with conn:
		cursor=conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS Student (Username TEXT,Name TEXT,Area TEXT,Programs INT,Fecha TEXT)')
	cursor.execute('INSERT INTO Student (Username,Name,Area,Programs,Fecha) VALUES(?,?,?,?,?)',(username,passw,sector,prog,time))
	conn.commit()
	sleep(1)
	Label(root, text= "Succesful Registration", fg="green", font =("bold",12)).place(x=180, y=450)
 	root.destroy() 


def main():
	Admin = admin.get()
	if (Admin == "oxana"):
		login.destroy()
		root= Tk()
		root.geometry('500x500')
		root.title("Nanotechnology Lab Registration")
		label_0 = Label(root, text="Nanotechnology \nLab Registration",width=20,font=("bold", 20))
		label_0.place(x=90,y=34)


		label_1 = Label(root, text="ID: ",width=20,font=("bold", 10))
		label_1.place(x=80,y=130)

		entry_1 = Entry(root,textvar=Username)
		entry_1.place(x=240,y=130)

		label_2 = Label(root, text="Name",width=20,font=("bold", 10))
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
	else: 
		messagebox.showinfo("Error", "Incorrect Password")




login = Tk()
Username = StringVar()
area = StringVar()
password = StringVar()
var1 = IntVar()
var2 = IntVar()
time = 0
admin = StringVar()
login.geometry('250x250')
login.title('Login')
label_5 = Label(login, text = "Enter admin \npassword:",width=12,font=("bold", 10))
label_5.place(x= 40, y = 100)
admin_entry = Entry(login, textvar = admin)
admin_entry.place(x= 60, y = 150)
admin_entry.config(show = "*")
Button(login, text='Ok',width=10,bg='brown',fg='white',command=main).place(x=80,y=190)

login.mainloop()
