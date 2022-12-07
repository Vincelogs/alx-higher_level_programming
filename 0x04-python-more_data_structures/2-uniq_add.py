#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_i = 0
    for n in set(my_list):
        sum_i += n
    return (sum_i)
