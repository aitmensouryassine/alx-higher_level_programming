#!/usr/bin/python3
""" Log parsing """
import sys


stats = {"size": 0, "200": 0, "301": 0, "400": 0,
         "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

try:
    for line in sys.stdin:
        stat = line.split(" ")

        status_code = stat[7]
        file_size = stat[8]

        stats[status_code] += 1
        stats["size"] += int(file_size)

        count += 1

        if count == 10:
            print("File size: {}".format(stats["size"]))
            for key in stats:
                if key != "size" and stats[key] != 0:
                    print("{}: {}".format(key, stats[key]))
            count = 0

except KeyboardInterrupt as err:
    print("File size: {}".format(stats["size"]))
    for key in stats:
        if key != "size" and stats[key] != 0:
            print("{}: {}".format(key, stats[key]))
