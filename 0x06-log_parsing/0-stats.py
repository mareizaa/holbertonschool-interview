#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
from sys import stdin

response_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

size = 0


def print_response():
    """Prints the accumulated logs"""
    print("File size: {}".format(size))
    for status in sorted(response_code.keys()):
        if response_code[status]:
            print("{}: {}".format(status, response_code[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                items = line.split()
                size += int(items[-1])
                if items[-2] in response_code:
                    response_code[items[-2]] += 1
            except:
                pass
            if count == 9:
                print_response()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_response()
        raise
    print_response()
