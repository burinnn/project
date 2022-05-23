# project
from tkinter import *

def annuitet(s,i,n):
    return int( s*(i / (10012)) /(1 - (1+i / (10012)) ** (-n)))

def credit():
    result = annuitet(int(e1.get())-int(e3.get()),int(e4.get()),int(e2.get()))
    e5.delete("0", END)
    e5.insert(0, result)
root = Tk()
root.title("Ипотека")
root.geometry("250x250")
root.configure(bg="lightblue")

l1 = Label(text="Сумма кредита",width=25)
e1 = Entry(width=25,bg="lightyellow")
l2 = Label(text="Срок",width=25)
e2 = Entry(width=25,bg="lightyellow")
l3 = Label(text="Первоначальный Взнос",width=25)
e3 = Entry(width=25,bg="lightyellow")
l4 = Label(text="Процент",width=25)
e4 = Entry(width=25,bg="lightyellow")
but = Button(text="Рассчитать Кредит",command=credit,width=25,bg="pink")
l5 = Label(text="Итог",width=25)
e5 = Entry(width=25,bg="lightyellow")
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()

l4.pack()
e4.pack()
but.pack()

l5.pack()
e5.pack()

root.mainloop()
