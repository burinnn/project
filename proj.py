from tkinter import *
import matplotlib, numpy, sys

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure




# подключение отрисовки внутри оконного интерфейса
matplotlib.use('TkAgg')

def annuitet(s,i,n):
    return int( s * (i / (12*100)) * (1 + i / (12*100))**(n) /((1 + i / (12*100)) ** (n) - 1) )


def credit():
    result = annuitet(int(e1.get())-int(e3.get()),int(e4.get()),int(e2.get()))
    e5.delete("0", END)
    e5.insert(0, result)

    # создаем область, внутри которой будет отображаться гистограмма платежей
    fig = Figure(figsize=(5,4), dpi=100)
    ax = fig.add_subplot(111) 

    # Считаем остаточное тело кредита по периодам
    data_body = numpy.array([(int(e1.get())-int(e3.get())) * (1 - (int(e4.get()) / (12*100)) /  ((1 + int(e4.get()) / (12*100)) ** (int(e2.get())) - 1) )**(k) for k in range(0, int(e2.get()) + 1)])
    
    #Считаем сумму платежа, приходящуюся на тело кредита
    data_rest_body = numpy.array( [data_body[indx - 1] - data_body[indx] for indx in range(1, int(e2.get()) + 1)] )

    # Рассчитывается полный ежемесячный платеж
    data_total = ( int(e5.get()), ) * int(e2.get())

    # Номера периодов (месяцев)
    ind = numpy.array([i for i in range(1, int(e2.get()) + 1)])

    width = 0.3 # Ширина столбцов
    

    rects_total = ax.bar(ind, data_total, width, label = "Процент кредита")
    rects_body = ax.bar(ind, data_rest_body, width, label = "Тело кредита")
    ax.legend()

    # Получение картинки гистограммы
    canvas = FigureCanvasTkAgg(fig,  master = root)
    canvas.get_tk_widget().place(x = 250, y = 250)



root = Tk()
root.title("Ипотека")
root.geometry("1000x800")
root.configure(bg="lightblue")

l1 = Label(text="Сумма кредита",width=25)
e1 = Entry(width=25,bg="lightyellow")
e1.insert(0, "0")

l2 = Label(text="Срок",width=25)
e2 = Entry(width=25,bg="lightyellow")
e2.insert(0, "0")

l3 = Label(text="Первоначальный Взнос",width=25)
e3 = Entry(width=25,bg="lightyellow")
e3.insert(0, "0")

l4 = Label(text="Процент",width=25)
e4 = Entry(width=25,bg="lightyellow")
e4.insert(0, "0")

but = Button(text="Рассчитать Кредит", command=credit, width=25, bg="pink")

l5 = Label(text="Итог",width=25)
e5 = Entry(width=25,bg="lightyellow")
e5.insert(0, "0")

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
