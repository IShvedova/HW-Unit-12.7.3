#Расчет депозита
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
val_per = list(per_cent.values())
TKB = int(val_per[0]*money/100)
SKB = int(val_per[1]*money/100)
VTB = int(val_per[2]*money/100)
SBER = int(val_per[3]*money/100)
deposit = ['TKB', 'SKB', 'VTB', 'SBER']
#num = int(val_per)
#profit = money * num
print ('Сумма, которую Вы можете заработать:', TKB, SKB, VTB, SBER)
print('Максимальная сумма, которую Вы можете заработать:', max(TKB, SKB, VTB, SBER))


