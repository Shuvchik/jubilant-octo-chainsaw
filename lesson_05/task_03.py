# Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        

SIZE = 10

fib = iter(fibonacci())

for _ in range(SIZE):
    print(next(fib))