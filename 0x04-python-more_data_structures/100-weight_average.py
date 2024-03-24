#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>)"""
    if not my_list:
        return 0

    total_weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return total_weighted_sum / total_weight
