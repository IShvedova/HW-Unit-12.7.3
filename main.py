# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада'))
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


