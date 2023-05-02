per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('money: '))
deposit = list()
for i in per_cent.values():
    deposit.append(i*money/100)
print(deposit)
print('Максимальная сумма, которую вы можете заработать: ', round(max(deposit), 2))
