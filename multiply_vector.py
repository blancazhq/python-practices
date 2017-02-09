list1 = [2, -9, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

new_list = []

for i in range(0, len(list1)):
    j = list1[i] * list2[i]
    new_list.append(j)

print new_list
