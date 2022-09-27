# Задача 9.
# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

print("Введите номер четверти от 1 до 4:")
chetvert = int(input())
while chetvert<1 or chetvert>4:
    print("Попробуйте снова:")
    chetvert = int(input())
if chetvert==1:
    print("x > 0 и y > 0")
elif chetvert==2:
    print("x < 0 и y > 0")
elif chetvert==3:
    print("x < 0 и y < 0")
else:
    print("x > 0 и y < 0")