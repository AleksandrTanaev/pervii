
import distutils.cygwinccompiler

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('введите сумму вклада:'))

A = money * per_cent.get('ТКБ')
Bank1 = A/100
B = money * per_cent.get('СКБ')
Bank2 = B/100
C = money * per_cent.get('ВТБ')
Bank3 = C/100
D = money * per_cent.get('СБЕР')
Bank4 = D/100

deposit = [Bank1, Bank2, Bank3, Bank4]
print(list(map(int, deposit)))



# Инициализация переменной max_deposit
max_deposit = deposit[0]

# Цикл for для прохода по всем элементам списка
for number in deposit:
    if number > max_deposit:
        max_deposit = number

# Вывод максимального числа
print("Максимальная сумма, которую вы можете заработать:", int(max_deposit))