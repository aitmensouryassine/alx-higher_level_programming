#!/usr/bin/python3
""" Log parsing """
import sys


def print_stats(stats):
    """ prints stats """

    print("File size: {}".format(stats["size"]))
    for key in sorted(stats):
        if key != "size" and stats[key] != 0:
            print("{}: {}".format(key, stats[key]))


if __name__ == "__main__":
    stats = {"size": 0, "200": 0, "301": 0, "400": 0,
             "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(stats)
                count = 1
            else:
                count += 1

            stat = line.split()

            try:
                status_code = stat[-2]
                file_size = stat[-1]
                stats["size"] += int(file_size)
            except Exception:
                pass

            if status_code in stats:
                stats[status_code] += 1
            status_code = 0

        print_stats(stats)

    except KeyboardInterrupt as err:
        print_stats(stats)
        raise
