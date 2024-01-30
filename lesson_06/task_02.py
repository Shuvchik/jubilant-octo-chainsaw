# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# from random import randint


# NUMBER_CONSTELLATIONS = 4
# NUMBER_QUEENS = 5


# def are_queens_attacking_each_other(queens: list(tuple())):
#     for i in range(len(queens)):
#         for j in range(i+1, len(queens)):
#             if queens[i][0] == queens[j][0] or \
#                queens[i][1] == queens[j][1] or \
#                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
#                return False
#     return True


# def position_generation() -> list:
#     result = []
#     queens = []
#     count = 0

#     while count != NUMBER_CONSTELLATIONS:
#         for _ in range(NUMBER_QUEENS):
#             queens.append((randint(1,8), randint(1,8)))
#         if are_queens_attacking_each_other(queens):
#             result.append(queens)
#             count += 1
#         queens = []

#     return result



# if __name__ == '__main__':
#     for i, value in enumerate(position_generation(), 1):
#         print(f'{i} - {value}')

from modul_to_task2 import position_generation