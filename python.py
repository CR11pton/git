# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 +/* 2
# 5 6 -> 2 +/* 3


import math

c = int(input('Дайте произведение двух чисел: '))
b = int(input('Дайте сумму двух чисел: '))
x1 = None
x2 = None
D = None
a = 1
# x1 * x2 = b
# x1 + x2 = c
# x1 = b - x2
# (b - x2) * x2 = c
#  b*y - x2*x2 = c
# x2*x2 - b*x2 + c = 0
# a*x2*x2 + (-b)*x2 + = 0
# Решаем квадратную уровнению через дискриминант

D = ((b*b) - (4*a*c))
round(D)
if D > 0:
    x1 = ((-(-b)) + math.sqrt(D))/(2*a)
    round(x1)
# 1 Так как a = 1
    x2 = ((-(-b)) - math.sqrt(D))/(2*a)
    round(x2)
    print(f'Первое число {x1}')
    print(f'Второе число {x2}')
elif D == 0:
    # x1 = x2
    x1 = (-(-b)/(2*a))
    round(x1)
    print(f'x1=x2: {x1}')
else:
    print('Таких чисел не существует')

