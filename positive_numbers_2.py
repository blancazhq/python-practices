#Given an list of numbers, print each number in the list that is greater than zero.

list = [2, -9, 3, 4, 5]

new_list = []

for i in list:
    if i > 0:
        new_list.append(i)

print new_list
