#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    arr = []

    for i in my_list:
        if i not in arr:
            arr.append(i)
    for i in arr:
        sum = sum + i
    return sum
