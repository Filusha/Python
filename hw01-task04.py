# Task 04.
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#

vl_num_in = list(input("Введите число: "))
vn_num_len = len(vl_num_in)
vn_max = 0
vn_cnt = 0
while True:
    if vn_cnt < vn_num_len:
        vn_max = max(vn_max, int(vl_num_in[vn_cnt]))
        vn_cnt = vn_cnt + 1
    else:
        break
print("Наибольшая цифра встреченная в числе: ", vn_max)
    