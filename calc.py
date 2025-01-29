import tkinter as tk

def get_values():
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    return n1, n2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    n1, n2 = get_values()
    res = n1 + n2
    insert_values(res)

def sub():
    n1, n2 = get_values()
    res = n1 - n2
    insert_values(res)

def mul():
    n1, n2 = get_values()
    res = n1 * n2
    insert_values(res)

def div():
    n1, n2 = get_values()
    res = n1 / n2
    insert_values(res)

window = tk.Tk() # окно
window.title('Калькулятор') # название
window.geometry("400x500")  # размер
window.resizable(False, False)  # неизменять размер окна
button_add = tk.Button(window, text = '+', width=2, height=2, command=add) #кнопки
button_add.place(x=110, y=300)
button_sub = tk.Button(window, text = '-', width=2, height=2, command=sub)
button_sub.place(x=160, y=300)
button_mul = tk.Button(window, text = '*', width=2, height=2, command=mul)
button_mul.place(x=210, y=300)
button_div = tk.Button(window, text = '/', width=2, height=2, command=div)
button_div.place(x=260, y=300)
num1_entry = tk.Entry(window, width=33)  # текстовое поле
num1_entry.place(x=100, y=75)
num2_entry = tk.Entry(window, width=33)
num2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=33)
answer_entry.place(x=100, y=400)
num1 = tk.Label(window, text="Введите первое число:")  # текстовое поле
num1.place(x=100, y=50)
num2 = tk.Label(window, text="Введите второе число:")
num2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=375)
window.mainloop()  # обновление событий в окне калькулятора
