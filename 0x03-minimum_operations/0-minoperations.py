#!/usr/bin/python3
'''
calculates the fewest number
of operations needed to result in exactly n H characters in the file.
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
