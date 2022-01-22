# Task 02.
# vn_sec_in     - int секунды введенные пользователем
# vn_sec_day    - int общее кол-во секунд текущего дня
# vn_hour       - int часы
# vn_min        - int минуты
# vn_sec        - int секунды
# секунды за час 60*60 = 3600
# секунды за день 24*60*60 = 84600

vn_sec_in = int(input("Введите секунды для конвертации: "))

vn_sec_day = vn_sec_in % 84600
vn_hour = vn_sec_day // 3600
vn_sec = vn_sec_day % 3600
vn_min = vn_sec // 60
vn_sec = vn_sec % 60

print("Текущее время: %02d:%02d:%02d" % ( vn_hour, vn_min, vn_sec ) )
