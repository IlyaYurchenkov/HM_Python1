# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти от 1 до 4: '))
print('Номер четверти: {}'.format(a))
if (a == 1):
    print('X<0 и Y>0')
elif (a == 2):
    print('X>0 и Y>0')
elif (a == 3):
    print('X<0 и Y<0')
elif (a == 4):
    print('X<0 и Y<0')
else:
    print ('Нет такой четверти')
