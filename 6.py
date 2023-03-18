# задача 30
a, d, n = int(input('1-й элемент: ')), int(input('Разность: ')), int(input("Кол-во элем-ов: ")),
c = [a]


def arithmetic_progression(a, d, n, k=1):
    if n == k:
        return 1
    a2 = a + k * d
    c.append(a2)
    arithmetic_progression(a2, a2 - a, n, k + 1)


arithmetic_progression(a, d, n)
print(c)

#задача 32
def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """
    from_min_to_max = []
    for i in range(len(num_lst)):
        if num_lst[i] > min_num and num_lst[i] < max_num:
            from_min_to_max.append(i)
    return from_min_to_max


print(is_in_mass(list(map(int, input("list: ").split())), int(input("min_num: ")), int(input("max_num: "))))