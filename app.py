#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Time comparison of algorithms that calculate the sum of integers in the interval [a, b]."""

import time


def iterative_sum(num_list):
    """Calculate the sum using a for loop and acumulator variable."""
    start_time = time.time()
    total = 0
    for num in num_list:
        total += num
    lapsed_time = time.time() - start_time
    return total, lapsed_time


def standart_sum(num_list):
    """Calculate the sum using standart 'sum' function of python."""
    start_time = time.time()
    total = sum(num_list)
    lapsed_time = time.time() - start_time
    return total, lapsed_time


def gauss_sum(num_list):
    """Calculate the sum using the Gauss formula: Sn = n * (f + l) / 2."""
    start_time = time.time()
    size_list = len(num_list)
    first_num = num_list[0]
    last_num = num_list[-1]
    total = size_list * (first_num + last_num) / 2
    lapsed_time = time.time() - start_time
    return int(total), lapsed_time


def main():
    """Time comparison of algorithms that calculate the sum of integers in the interval [a, b]."""
    print(
        "Time comparison of algorithms that calculate the sum of integers in the interval [a, b]."
    )
    print('----------------------------------------------------------')
    first_num = 100
    last_num = int(1e6)
    big_list = list(range(first_num, last_num + 1))
    print(
        f'Ordenered list: [{first_num}, {first_num + 1}, ..., {last_num - 1}, {last_num}]'
    )
    print(f'size of list is {len(big_list)}')
    print('----------------------------------------------------------')
    total1, lapsed_time1 = iterative_sum(big_list)
    total2, lapsed_time2 = standart_sum(big_list)
    total3, lapsed_time3 = gauss_sum(big_list)
    lap_time_format1 = "{:.10f}".format(lapsed_time1)
    lap_time_format2 = "{:.10f}".format(lapsed_time2)
    lap_time_format3 = "{:.10f}".format(lapsed_time3)
    print('Algorithm\tSum\t\tLapsed time')
    print(f'Iterative sum\t{total1}\t{lap_time_format1}s')
    print(f'Standart sum\t{total2}\t{lap_time_format2}s')
    print(f'Gauss sum\t{total3}\t{lap_time_format3}s')


if __name__ == '__main__':
    main()
