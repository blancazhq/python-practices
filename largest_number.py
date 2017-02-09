#Given an list of numbers, print the largest of the numbers.

list = [-1, 9, 3, 4, 5]

max = list[0]

for i in list:
    if i > max:
        max = i

print max
