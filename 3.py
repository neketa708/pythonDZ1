"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint
a = randint(0, 1000)
n = 0
while n!=10:
    b = int(input("введите число "))
    if a==b:
        print("вы угадали")
        break
    elif a>b:
        print("загадонное число больше")
        n+=1
        print(f"попыток {n} из 10")
    else:
        print("загадонное число меньше")
        n+=1
        print(f"попыток {n} из 10")
print("не угадали")