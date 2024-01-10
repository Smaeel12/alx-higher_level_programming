#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    weight_sum = 0
    mul_sum = 0
    for eset in my_list:
        mul_sum += eset[0] * eset[1]
        weight_sum += eset[1]
    average_weight = mul_sum / weight_sum
    return average_weight
