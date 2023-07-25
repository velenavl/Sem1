# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

STEP = 2

n = 10
e = 3

count = 0
summ_nums = 0

while count <= n:
    if count % e != 0:
        summ_nums += count
        print(count, summ_nums)
    count += STEP

print(summ_nums)
