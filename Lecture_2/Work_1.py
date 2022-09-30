# модуль a - открытие создание, добавление записи
# модуль w - открытие , перезапись записи
# модуль r - открытие , чтение записи

colors = ['red', 'green', 'blue3']
data = open('file.txt', 'a')
# data.writelines(colors) #разделителей не будет
data.write('\nline 1\n')
data.write('line 1\n')
data.close()

# вариант другой записи модулей
# with open('file.txt', 'w') as data:
#   data.write('line 1\n')
#   data.write('line 2\n')

exit()
