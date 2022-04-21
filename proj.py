from tkinter import *



def credit():
  result = int(e1.get()) * int(e2.get())e3.get()
  e4.clipboard_clear()
  e4.insert(0, result)


root = Tk()
l1 = Label(text="Сумма кредита")
e1 = Entry(width=50, bg='black', fg='white')
l2 = Label(text="Срок")
e2 = Entry(width=50, bg='black', fg='white')
l3 = Label(text="Первоначальный взнос")
e3 = Entry(width=50, bg='black', fg='white')
but = Button(text="Рассчитать кредит",command=credit)
l4 = Label(text="ИТОГ")
e4 = Entry(width=50, bg='black', fg='white')
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
but.pack()
l4.pack()
e4.pack()


root.mainloop()
