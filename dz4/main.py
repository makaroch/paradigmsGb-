from typing import List

def correlation(lst1: List, lst2: List) -> int:
    if len(lst1) != len(lst2):
        raise Exception
    arithmetic_mean1 = sum(lst1) / len(lst1)
    arithmetic_mean2 = sum(lst2) / len(lst2)
    first_summ = 0
    second_summ = 0
    for i in range(len(lst2)):
        first_summ += (lst1[i] - arithmetic_mean1) * (lst2[i] - arithmetic_mean2)
        second_summ += ((lst1[i] - arithmetic_mean1)**2) * ((lst2[i] - arithmetic_mean2)**2)
    return first_summ / (second_summ ** 0.5)


