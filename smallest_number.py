#Given an list of numbers, print the smallest of the numbers.

list = [-1, 9, 3, -4, 5]

min = list[0]

for i in list:
    if i < min:
        min = i

print min
