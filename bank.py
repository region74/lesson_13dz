import json


def check_balance(has_money, price):
    if price > has_money:
        print('Недосточно средств!\n')
        return False
    else:
        return True


def read_balance():
    with open('balance.json', 'r') as f:
        return int(json.load(f))


def write_balance(balance):
    with open('balance.json', 'w') as f:
        json.dump(balance, f)
        return None


def read_list():
    with open('orders.json', 'r') as f:
        return list(json.load(f))


def write_list(list_payments):
    with open('orders.json', 'w') as f:
        json.dump(list_payments, f)
        return None


while True:
    balance = read_balance()
    list_payments = read_list()

    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Текущий баланс: {balance}\n')

    choice = input('Выберите пункт меню: \n')
    if choice == '1':
        cost = int(input('Введите сумму: '))
        balance += cost
        write_balance(balance)
    elif choice == '2':
        price = int(input('Введите стоимость покупки: '))
        if check_balance(balance, price):
            purchase_name = input('Введите название покупки: ')
            list_payments.append((purchase_name, price))
            write_list(list_payments)
            balance -= price
            write_balance(balance)
    elif choice == '3':
        print(read_list())
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
