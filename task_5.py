'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |'''

nums = int(input('Введите трехзначное число: '))
first_number = nums//100
second_number = (nums // 10) % 10.
third_number = nums % 10
print(f"Сумма цифр трехзначного числа = {first_number + second_number + third_number}")