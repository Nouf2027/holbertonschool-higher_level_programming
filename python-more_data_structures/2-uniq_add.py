#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = []
    total = 0

    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)

    for num in unique_numbers:
        total += num

    return total
