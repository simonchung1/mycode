#!/usr/bin/env python3

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for y in list1:
    if y > 150:
        break
    if y % 5 == 0:
        print(y)

