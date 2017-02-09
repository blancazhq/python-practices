#Given an list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. 

list = [2, -9, 3, 4, 5]

factor = 3

new_list = []

for i in list:
        new_list.append(i * factor)

print new_list
