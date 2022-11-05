from tkinter import *
import tkinter as tk
from tkinter import ttk

top=Tk()
top.geometry("800x500")
top.configure(background="lightblue")

f_name=StringVar()
l_name=StringVar()
E_mail=StringVar()
zip_code=IntVar()


def insert():
    value=''
    for i in value:
        lb2.insert("end", i)
        
        
lb=Listbox(top,width=50,height=22)
lb.place(x=20,y=30)


lb1=Listbox(top,width=50,height=22)
lb1.place(x=470,y=30)

b=Button(top,text="Insert" ,width=10,command=insert)
b.place(x=360,y=120)

b1=Button(top,text="Delete" ,width=10)
b1.place(x=360,y=180)

b2=Button(top,text="Theme" ,width=10)
b2.place(x=360,y=240)

l=Label(top,text="First Name:",background="white" )
l.place(x=30,y=40)

e=Entry(top,textvariable=f_name,font=('Arial',10,'normal'))
e.place(x=110,y=40)

l=Label(top,text="Last Name:",background="white")
l.place(x=30,y=70)

e1=Entry(top,textvariable=l_name,font=('Arial',10,'normal'))
e1.place(x=110,y=70)

l1=Label(top,text="Gender:",background="white")
l1.place(x=30,y=100)

r=Radiobutton(top, text='Male', value='Value 1',background='white')
r.place(x=110,y=100)

r1=Radiobutton(top, text='Female', value='Value 2',background='white')
r1.place(x=170,y=100)


l2=Label(top,text="Languages:",background="white")
l2.place(x=30,y=130)

c=Checkbutton(top,text='Telugu',background='white')
c.place(x=110,y=130)

c1=Checkbutton(top,text='English',background='white')
c1.place(x=180,y=130)

c2=Checkbutton(top,text='Hindi',background='white')
c2.place(x=250,y=130)

l3=Label(top,text="Email:",background="white")
l3.place(x=30,y=160)

e2=Entry(top,textvariable=E_mail,background='white')
e2.place(x=110,y=160)

l4=Label(top,text="Adress:",background="white")
l4.place(x=30,y=190)

lb2=Listbox(top,width=25,height=5)
lb2.place(x=110,y=190)

l5=Label(top,text="State:",background="white")
l5.place(x=30,y=280)

li1=Listbox(top,bg="white",activestyle="dotbox",font=("arial",10),height=1,width=15)
li1.place(x=110,y=280)
li1.insert(1,"Choose State")


l6=Label(top,text="Zip:",background="white")
l6.place(x=30,y=310)

e2=Entry(top,textvariable=zip_code,font=('Arial',10,'normal'))
e2.place(x=110,y=310)

l7=Label(top,text="Credit Card Type:",background="white")
l7.place(x=30,y=340)

li1=Listbox(top,bg="white",activestyle="dotbox",font=("arial",10),height=1,width=20)
li1.place(x=140,y=340)
li1.insert(1,"Choose Credit card")


l8=Label(top,text='Billing Records',background='silver',height=1,width=19,font=('Arial','20'))
l8.place(x=470,y=20)

top.mainloop()