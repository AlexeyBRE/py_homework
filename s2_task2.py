'''Задача 12
 Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
помогает Кате по математике. Он задумывает два натуральных числа X и Y
(X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
задуманные Петей числа.'''

s = int(input("Сумма чисел: "))
p = int(input("Произведение чисел: "))
x = s//2
y = p/x
print(f"Первое число равно: {x} , второе чило равно {y}")



