#!/usr/bin/env python3
# coding:utf-8

def rearrange(lst):
    lst.sort()
    n = len(lst)
    if n < 3:
        return lst
    lst2 = []
    i = 0
    j = (n - 1) // 2 if n % 2 == 0 else n // 2
    for k in range(2):
        lst2.append(lst[j])
        j += 1
    for k in range(2, n):
        if k % 2 == 0:
            lst2.append(lst[i])
            i += 1
        else:
            lst2.append(lst[j])
            j += 1

    return lst2


lst = [1, 5, 3, 6, 8, 10, 15, 22, 17, 9, 2, 3, 4]
print(rearrange(lst))





