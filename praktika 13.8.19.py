ticket = int(input('Введите колличество билетов для покупки: '))
ages = []

for i in range(0, ticket):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    ages.append(input_value)
    def prise(age):
        if age < 18:
            return 0
        elif 18 < age < 25:
            return 990
        else:
            return 1390

fullsum = sum(map(prise, ages))
discountsum = int(fullsum * 0.9)

if ticket > 3:
    print('Стоимость всех билетов со скидкой: ', discountsum, "руб.")
else:
    print('Стоимость всех билетов: ', fullsum, "руб.")


