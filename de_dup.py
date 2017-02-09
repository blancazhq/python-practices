#Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.
#the most difficult thing for me is to set up the handler, when the target number compare through all numbers before it, the handler toggles.

list = [2, 2, 4, -9]

new_list = []

repeat = False

for i in range(0, len(list)):
    for j in range(0, i):
        if list[i] == list[j]:
            repeat = True
    if repeat == False:
        new_list.append(list[i])
    repeat = False

print new_list
