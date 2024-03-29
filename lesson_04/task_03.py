# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import time

def refill_withdraw(balance, count, mode, commission):
    '''Функция изменения счета в зависимости от режима работы - снятие/пополнение'''

    global history_operations

    money_commission = 0 + commission

    while True:
        money = int(input('Введите сумму пополнения (кратную 50): '))
        if money % 50 == 0:
            break
        else:
            print('Повторите попытку')

    if count == 3: 
        money_commission += 0.03

    match mode:
        case 1:
            money_value = (money - (money * money_commission))
            balance += money_value
            history_operations.append(f'Пополнение баланса +{money_value}')
        case 2:
            if money > balance:
                print('Ошибочная операция!')
                return balance
            if money * (0.015 + money_commission) <= 30:
                money_value = (money + 30)
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')
            elif money * (0.015 + money_commission) >= 600:
                money_value = (money + 600)
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')
            else:
                money_value = (money + (money * (0.015 + money_commission)))
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')

    return balance

def print_history_operation():
    '''Печатает историю операций по счету'''

    global history_operations

    print('\n')
    for number, value in enumerate(history_operations, 1):
        print(f'{number}. {value}')


balance = 0
number_operations = 0
money_commission = 0
history_operations = []

while True:
    print(f'\nВведите номер операции:\n'
      '1. Пополнить счет\n'
      '2. Снять деньги\n'
      '3. Показать баланс\n'
      '4. История операций\n'
      '5. Выйти\n')
    
    mode = int(input('Введите номер операции: ')) 

    if balance >= 5_000_000:
        money_commission = 10

    match mode:
        case 1:
            balance = refill_withdraw(balance, number_operations, mode, money_commission)
            number_operations += 1
        case 2:
            if balance != 0:
                balance = refill_withdraw(balance, number_operations, mode, money_commission)
                number_operations += 1
            else:
                print('Нулевой баланс!')
        case 3:
            print(f'\nВаш баланс: {balance}')
            time.sleep(2)
        case 4:
            print_history_operation()
            time.sleep(2)
        case 5:
            break