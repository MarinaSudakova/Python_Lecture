my_list = []

# можно заполнить циклом for или comprehentions
# for i in range(1, 101):
#     if(i%2 == 0):
#         my_list.append(i)

my_list = [i for i in range(1,101) if i % 2 == 0]

print(my_list)

# применять действие внутри
def f(x):
    return x ** 2

second_list = [f(i) for i in range(1,21) if i % 2 == 0]
print(second_list)