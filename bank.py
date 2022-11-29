import json


def check_balance(has_money, price):
    if price > has_money:
        print('Недосточно средств!\n')
        return False
    else:
        return True


while True:
    with open('balance.json', 'r') as f:
        balance = json.load(f)
    with open('orders.json', 'r') as f:
        list_payments = json.load(f)

    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Текущий баланс: {balance}\n')

    choice = input('Выберите пункт меню: \n')
    if choice == '1':
        cost = int(input('Введите сумму: '))
        balance += cost
        with open('balance.json', 'w') as f:
            balance = json.dump(balance, f)

    elif choice == '2':
        price = int(input('Введите стоимость покупки: '))
        if check_balance(balance, price):
            purchase_name = input('Введите название покупки: ')
            list_payments.append((purchase_name, price))
            with open('orders.json', 'w') as f:
                json.dump(list_payments, f)
            balance -= price
            with open('balance.json', 'w') as f:
                balance = json.dump(balance, f)

    elif choice == '3':
        with open('orders.json', 'r') as f:
            list_payments = json.load(f)
            print(list_payments)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
