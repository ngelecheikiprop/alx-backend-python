#!/usr/bin/env python3
'holds function that return sums of float'
from typing import List


def sum_list(input_list: List[float]) -> float:
    'takes list of float and returns sum as float'
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
