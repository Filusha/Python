# Task 03.
# Узнать у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Используется длинное решение
# Можно короче, без приведения типов
# >> vs_num_in = input("Введите число: ")
# >> print("Результат: " + str(eval( vs_num_in + " + " + vs_num_in*2 + " + " + vs_num_in*3 )))

vn_num_in = int(input("Введите число: "))
vs_expression = str(vn_num_in) + " + " + str(vn_num_in)*2 + " + " + str(vn_num_in)*3
vn_rezult = eval(vs_expression)
print("Результат: " + str(vn_rezult))