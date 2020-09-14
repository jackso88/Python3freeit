import math
from tkinter import *
from decimal import *

#Создаю окно
root = Tk()
root.title("Calc на Python")
root.geometry("570x300")

#Создание поля вывода
screen = Label(text = '0', justify = LEFT, font="Arial 16")
screen.place( x = 10, y = 50)

#Создание кнопок с использованием цикла
buttons = (
		   ('7', '8', '9', '/', '%', 'C', '<--', 'M'),
           ('4', '5', '6', '*', 'x^', 'sin(x)', 'log(x,y)', 'MR'),
           ('1', '2', '3', '-', 'sqrt', 'cos(x)', 'log2', 'MC'),
           ('0', '.', '-/+', '+', 'x!', 'tg(x)', 'log10', '='),
           )

for elements in buttons: 
	for el in elements:   
		btn = Button(
		root, 
		text = buttons[buttons.index(elements)][elements.index(el)],
		command = lambda row = buttons.index(elements),
		col = elements.index(el): press_btn(buttons[row][col])
		)
		btn.grid(
		row = buttons.index(elements) + 7, 
		column = elements.index(el), 
		ipadx = 9, ipady = 7, padx = 1, pady = 1, sticky = "nsew"
		)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(7, weight=6)

#Списки и пересенные для хранения данных 
lst = []
result = ''
gap = ''
mem = ''

#Функция для обработки нажатия кнопок
def press_btn(x):
	global result
	global lst
	global gap
	global mem
	if x == 'C':
		result = '0'
		lst.clear()
		gap = ''
		screen.configure(text = result)
	if '0' <= x <= '9':
		if result == '0' or result == '':
			result = ''
			result += x
			screen.configure(text = result)
		else:
			result += x
			screen.configure(text = result)
	elif x == '.' and x not in result:
		if result == '':
			result = '0'
		result += x
		screen.configure(text = result)
	elif x == '<--' and result != '0':
		result = result[:-1]
		screen.configure(text = result)
		if gap != '':
			gap = gap[:-1]
			screen.configure(text = gap)
	elif x == '-/+':
		if gap != '':
			if float(gap) > 0:
				gap = '-' + gap
				screen.configure(text = gap)
			else:
				gap = gap[1:]
				screen.configure(text = gap)
		elif result[0] == '-':
			result = result[1:]
			screen.configure(text = result)
		else:
			if result != '0':
				result = '-' + result
				screen.configure(text = result)
	if x == 'M':
		if gap != '':
			mem = gap
		else:
			mem = result
	if x == 'MC':
		mem = ''
	if x == 'MR':
		result = mem
		screen.configure(text = result)
	if x in [
			 'tg(x)', 'cos(x)', 'sin(x)', 'sqrt', 'log10', 'log2', 'x!'
			 ]:
		if result != '':
			lst.append(result)
		else:
			lst.append(gap)
			gap = ''
		lst.append(x)
		lst.append('0')
		calculate()
		gap = result
		result = ''
	if x in [
			 '+', '-', '*', '/', 'x^', '%', 'log(x,y)'
			 ]:
		if len(lst) == 2:
			if gap != '':
				lst.append(gap)
			else:
				lst.append(result)
			calculate()
			lst.append(result)
			lst.append(x)
		if len(lst) == 0:
			if gap != '':
				if result == '':
					lst.append(gap)
				else:
					lst.append(result)
			else:
				lst.append(result)
			lst.append(x)
		gap = ''
		result = ''
	if x == '=' and len(lst) >= 2:
		lst.append(result)
		calculate()
		gap = result
		result = ''
		
#Функция для расчета значений
def calculate():
	global lst
	global result
	second = lst.pop()
	i = lst.pop()
	first = lst.pop()
	if i == '+':
		result = str(Decimal(first) + Decimal(second))
		screen.configure(text = result)
	if i == '-':
		result = str(Decimal(first) - Decimal(second))
		screen.configure(text = result)
	if i == '*':
		result = str(Decimal(first) * Decimal(second))
		screen.configure(text = result)
	if i == '/':
		if Decimal(second) == 0:
			result = ''
			screen.configure(text = 'Division by zero')
		else:
			result = str(Decimal(first) / Decimal(second))
			screen.configure(text = result)
	if i == 'x^':
		result = str(Decimal(first) ** Decimal(second))
		screen.configure(text = result)
	if i == '%':
		result = str(Decimal(first) * Decimal((Decimal(second) / 100)))
		screen.configure(text = result)
	if i == 'sqrt':
		result = str(Decimal(math.sqrt(Decimal(first))))
		screen.configure(text = result)
	if i == 'sin(x)':
		result = str(Decimal(math.sin(Decimal(first))))
		screen.configure(text = result)
	if i == 'cos(x)':
		result = str(Decimal(math.cos(Decimal(first))))
		screen.configure(text = result)
	if i == 'tg(x)':
		result = str(Decimal(math.tan(Decimal(first))))
		screen.configure(text = result)
	if i == 'log10':
		result = str(Decimal(math.log10(Decimal(first))))
		screen.configure(text = result)
	if i == 'log2':
		result = str(Decimal(math.log2(Decimal(first))))
		screen.configure(text = result)
	if i == 'log(x,y)':
		result = str(Decimal(math.log(Decimal(first), Decimal(second))))
		screen.configure(text = result)
	if i == 'x!':
		if Decimal(first) >= 2500 or Decimal(first) < 0:
			result = ''
			screen.configure(text = 'Incorrect value')
		else:
			result = str(math.factorial(round(float(first),0)))
			screen.configure(text = result)
		
#Запуск всего этого добра
root.mainloop()
