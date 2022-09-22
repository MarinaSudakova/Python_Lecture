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