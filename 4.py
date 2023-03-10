# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.

first_list = set(list(map(int, input('1 list: ').split())))
second_list = set(list(map(int, input('2 list: ').split())))
print(sorted(first_list.intersection(second_list)))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке содержащим количество ягод на кустах.
#
#
# Input: 2 2 1 3 2
# Output: 7

a = (list(map(int, input('введите кол-во ягод, через _пробел_ ').split())))
maximum = 0
for i in range(len(a)-1):
    a_i = a[i - 1] + a[i] + a[i + 1]
    if a_i > maximum:
        maximum = a_i
    if i == (len(a) - 2):
        a.append(a[0])
        i = i + 1
        a_i = a[i - 1] + a[i] + a[i + 1]
        if a_i > maximum:
            maximum = a_i
print(maximum)