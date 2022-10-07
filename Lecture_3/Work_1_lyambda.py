# переменной можно присовить всю функцию

def f(x):
    return x ** 2

g = f

print(type(f))
print(type(g))

print(f(4))
print(g(4))

# фнкуция принимает любую другую функцию в качестве параметра

def math (op, x):
    print(op(x))

math(f, 10)

# лямбда - укороченное написание функции
f = lambda q: q + 20

math(f, 3)
math(lambda q: q + 21, 3)