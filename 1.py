print('***** Задача 2 *****') 
# : Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
data = map(int, " ".join(input('введите трехзначное число: ')).split())
print(f'сумма: {sum(data)}')

print("*** Задача 4 ***")
# : Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"
S = input('общее кол-во журавлей -> ')
for i in S:
    if i.isalpha() or i == '-':
        print("Неверное S")
        break
else:
    if int(S)%6 != 0:
        print("Неверное S")
    else:
        x = int(S) // 3
        print(f'Петя: {x//2}, Катя: {2 * x}, Сережа: {x//2}')


print("*** Задача 6 ***")
# : Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
ticket = list(map(int, (input())))
if sum(ticket[0:3]) == sum(ticket[3:]):
    print(f'билет № {"".join(map(str, ticket))} - yes!')
else:
    print(f'билет № {"".join(map(str, ticket))} - no!')

#
# 385916 -> yes
# 123456 -> no
print("*** Задача 8 ***") 
# Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
m, n, k = list(map(int, input("введите m, n, k через пробел: ").split()))
if (k % m == 0 or k % n == 0) and k <= m*n:
    print(f'{m} x {n} x {k} -> yes')
else:
    print(f'{m} x {n} x {k} -> no')
#
# 3 2 4 -> yes
# 3 2 1 -> no