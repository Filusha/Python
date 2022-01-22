# Task 05.
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# vf_revenue_in     - выручка
# vf_expenses_in    - издержки
# vf_profit         - прибыль
# vf_loss           - убыток

vf_revenue_in = float(input("Введите величину выручки отчетного периода: "))
vf_expenses_in = float(input("Введите величину издержек отчетного периода: "))

if vf_revenue_in > vf_expenses_in:
    vb_is_profit = True
    vf_profit = round(vf_revenue_in - vf_expenses_in, 2)
    print("Прошедший отчетный период завершен с прибылью - ", vf_profit )
else:
    vb_is_profit = False
    vf_loss = round(vf_expenses_in - vf_revenue_in, 2)
    print("Прошедший отчетный период завершен с убытками - ", vf_loss)

# Task 6.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
vf_return_on_revenue = float(0)
vf_profit_per_staff = float(0)

if vb_is_profit:
    vf_return_on_revenue = round((vf_profit / vf_revenue_in)*100, 2)
    vn_staff_cnt = int(input("Введите кол-во сотрудников фирмы: "))
    vf_profit_per_staff = round(vf_profit / vn_staff_cnt, 2)
    print("Рентабельность выручки - ", vf_return_on_revenue)
    print("Прибыль в расчете на сотрудника - ", vf_profit_per_staff)