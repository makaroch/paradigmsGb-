def sort_list_imperative(lst):
    for i in range(len(lst) - 1):
        count = 0
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                count += 1
        if count==0:
            return 


def sort_list_declarative(lst: list):
    lst.sort()