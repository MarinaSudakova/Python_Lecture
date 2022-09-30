import Work_3 as h

print(h.f(1))

# возможности функций
def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!! заменил второй аргумент на указанный
print(new_string('!')) # !!!
print(new_string(4)) # 12 прочитал символ как число

# неограниченное количество параметров
def concatenatio(*params):
    res: str = ''
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))