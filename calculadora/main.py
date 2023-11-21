from tkinter import *
from tkinter import ttk


c1 = "#dddddd" #branco
c2 = "#000000" #preto
c3 = "#f48422" #Laranja
c4 = "#474746" #Cinza Escuro


win =Tk()
win.title("Calculadora daora")
win.geometry("235x318")
win.config(bg=c2)


#divisão de abas
frame_win = Frame(win, width=235, height=56, bg=c4)
frame_win.grid(row=0, column=0)


frame_bd = Frame(win, width=235, height=268)
frame_bd.grid(row=1, column=0)

#variable

every_value = ''

#calculadora
def calculadora(value):
    global every_value
    every_value = every_value + str(value)
    text_value.set(every_value)


def calcular():
    global every_value
    result = eval(every_value)
    text_value.set(result)
    


def clear():
    global every_value
    every_value =""
    text_value.set("")


text_value = StringVar()

app_label = Label(frame_win, textvariable=text_value, width=16, height=2, bg=c4, fg=c1, padx=7, anchor="e", justify=RIGHT, font=('Arial 18'))
app_label.place(x=0,y=0)


#botões superiores
bt_1 = Button(frame_bd, command=clear, text="C", width=11, height=2, bg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
bt_1.place(x=0, y=0)

bt_2 = Button(frame_bd, command = lambda: calculadora('/'), text="/", width=5, height=2, bg=c4, fg=c3, font=('Tahoma 13 bold'), relief=FLAT, overrelief=RIDGE)
bt_2.place(x=177, y=0)

#numerais
n_1 = Button(frame_bd, command = lambda: calculadora('7'), text="7", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_1.place(x=0, y=52)

n_2 = Button(frame_bd, command = lambda: calculadora('8'), text="8", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_2.place(x=59, y=52)

n_3 = Button(frame_bd, command = lambda: calculadora('9'), text="9", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_3.place(x=118, y=52)

n_4 = Button(frame_bd, command = lambda: calculadora('4'), text="4", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_4.place(x=0, y=104)

n_5 = Button(frame_bd, command = lambda: calculadora('5'), text="5", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_5.place(x=59, y=104)

n_6 = Button(frame_bd, command = lambda: calculadora('6'), text="6", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_6.place(x=118, y=104)

n_7 = Button(frame_bd, command = lambda: calculadora('1'), text="1", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_7.place(x=0, y=156)

n_8 = Button(frame_bd, command = lambda: calculadora('2'), text="2", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_8.place(x=59, y=156)

n_9 = Button(frame_bd, command = lambda: calculadora('3'), text="3", width=5, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_9.place(x=118, y=156)

n_0 = Button(frame_bd, command = lambda: calculadora('0'), text="0", width=11, height=2, bg=c1, fg=c3, font=('Tahoma 13 bold'), relief=GROOVE, overrelief=RIDGE)
n_0.place(x=0, y=211)

#laterais

bt_3 = Button(frame_bd, command = lambda: calculadora('*'), text="*", width=5, height=2, bg=c4, fg=c3, font=('Tahoma 13 bold'), relief=FLAT, overrelief=RIDGE)
bt_3.place(x=177, y=52)

bt_4 = Button(frame_bd, command = lambda: calculadora('-'), text="-", width=5, height=2, bg=c4, fg=c3, font=('Tahoma 13 bold'), relief=FLAT, overrelief=RIDGE)
bt_4.place(x=177, y=104)

bt_5 = Button(frame_bd, command = lambda: calculadora('+'), text="+", width=5, height=2, bg=c4, fg=c3, font=('Tahoma 13 bold'), relief=FLAT, overrelief=RIDGE)
bt_5.place(x=177, y=156)

bt_6 = Button(frame_bd, command = calcular, text="=", width=5, height=2, bg=c4, fg=c3, font=('Tahoma 13 bold'), relief=FLAT, overrelief=RIDGE)
bt_6.place(x=177, y=208)

bt_7 = Button(frame_bd, command = lambda: calculadora('.'), text=".", width=5, height=2, bg=c3, font=('Tahoma 12 bold'), relief=GROOVE, overrelief=RIDGE)
bt_7.place(x=119, y=211)

#aprender a fazer depois

#bt_8 = Button(frame_bd, command=percentage, text="%", width=5, height=2, bg=c4, fg=c3,font=('Ivy 13 bold'),relief=GROOVE, overrelief=RIDGE)
#bt_8.place(x=118, y=0)


win.mainloop()
