value = None
a = 123
b = 1.23
#print(type(a))
#print(type(b))
value = 2345
#print(type(value))

s = 'hello world'
#s = 'hello \nworld' переход на новую строку
print(a, b, s)
print(a, '-', b, '-', s)
print('{1} - {0} - {2}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
list = [1, 2, 3] #массив данных

print('Введите a'); #ввод данных от пользователя
a = int(input())

a = int(input('a = ')) #условие
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)


original = 23 #инверсия числа
inverted = 0
while original != 0:
    inerted = inverted * 10 + (original % 10)
    original // 10
print(inverted)

for i range(1, 10, 2): #цикл в порядке чисел от 1 до 9, с точкой хода 2
    print(i)



#работа со строками
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #

for c in text:
    print(c)

#работа с символами в строках
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#ведение списков
colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

#функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType