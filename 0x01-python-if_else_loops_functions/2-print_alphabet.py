#!/usr/bin/python3
txt = "{number:c}"
for c in range(97, (97 + 26)):
    print(txt.format(number=c), end="")
