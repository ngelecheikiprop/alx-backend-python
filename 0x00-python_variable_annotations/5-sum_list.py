#!/usr/bin/env python3
'holds function that return sums of float'


def sum_list(input_list: list[float]) -> float:
    'takes list of float and returns sum as float'
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum

