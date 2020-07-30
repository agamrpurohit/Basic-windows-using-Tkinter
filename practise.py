from tkinter import *

window=Tk()

def kgsto():
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    oz=float(e1_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    t3.delete("1.0",END)
    t3.insert(END,oz)




b1=Button(window,text="Convert", command=kgsto) 
b1.grid(row=1,column=6)   

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=1,column=3)

t1=Text(window,height=1,width=20)
t1.grid(row=2,column=1,rowspan=2)
t2=Text(window,height=1,width=20)
t2.grid(row=2,column=3,rowspan=2)
t3=Text(window,height=1,width=20)
t3.grid(row=2,column=5,rowspan=2)

window.mainloop()
