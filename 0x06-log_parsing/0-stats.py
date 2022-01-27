#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
from sys import stdin

reponse_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

t_size = {'size': 0}


def print_reponse():
    """Prints logs"""
    print("File size: {}".format(t_size['size']))
    for code in sorted(reponse_codes.keys()):
        if reponse_codes[code] > 0:
            print("{}: {}".format(code, reponse_codes[code]))



def result(item):
    """Operates with the resume stats"""
    try:
        item = item.split(' ')
        size = item[-1]
        t_size["size"] += int(size)
        if item[-2] in reponse_codes:
            reponse_codes[item[-2]] += 1
    except Exception as e:
        pass


if __name__ == '__main__':
    num_lines = 1
    try:
        for line in stdin:
            result(line)
            if num_lines % 10 == 0:
                print_reponse()
            num_lines += 1
    except KeyboardInterrupt:
        print_reponse()
        raise
    print_reponse()
