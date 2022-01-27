#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
from sys import stdin

if __name__ == "__main__":
    status_codes = {
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


    def print_stats():
        """Prints logs"""
        print("File size: {}".format(size))
        for status in sorted(status_codes.keys()):
            if status_codes[status]:
                print("{}: {}".format(status, status_codes[status]))



    count = 0
    try:
        for line in stdin:
            try:
                items = line.split()
                size += int(items[-1])
                if items[-2] in status_codes:
                    status_codes[items[-2]] += 1
            except:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()