#!/usr/bin/python3
'''
Given a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total
'''


def minOperations(n):
    ''' Minimum Operations '''
    min = 0
    i = 2
    while (i <= n):
        while (n % i == 0):
            min += i
            n /= i
        i += 1
    return (min)
