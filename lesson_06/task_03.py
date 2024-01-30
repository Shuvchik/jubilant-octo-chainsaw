# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей 
# в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

good_arrangements = position_generation()

print('Удачные расстановки: ')
for i, positions in enumerate(good_arrangements, 1):
    print(f'{i} - {positions}')