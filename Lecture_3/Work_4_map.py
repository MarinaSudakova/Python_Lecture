# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

my_list = [x for x in range(1, 21)]

print(my_list)

my_list = list(map(lambda x: x + 10, my_list))

print(my_list)

# функция мэп со считыванием

data = list(map(int, input().split()))
print(data)