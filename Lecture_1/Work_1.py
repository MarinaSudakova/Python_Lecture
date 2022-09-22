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