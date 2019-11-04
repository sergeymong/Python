def countdown(n):
    if n <= 0:
        print('Старт!')
    else:
        print(n)
        countdown(n-1)

countdown(5)


def do_n(func, n):
    func()
    do_n(func, n-1)


def check_ferma(a, b, c, n):
    if n > 2:
        if a ** n + b ** n == c ** 2:
            print("Невероятно, Ферма ошибся!")
        else:
            print("Нет, это не подходит")

check_ferma(1, 1, 1, 5)


def is_between(x, y, z):
    return x <= y <= z

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


print(factorial(5))


def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
