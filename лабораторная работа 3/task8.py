money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital > 0:
    money_capital = money_capital - spend + salary
    spend = spend * (1 + increase)
    month += 1
print(month - 1)
# в моем решении пременная month показывает на какой
# месяц у человека будет получаться отрицательный бюджет, сл-но
# прожить можно month - 1 месяц
