list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]

new_list1 = []
new_list2 = []


j1 = (list1[0])[0] * (list2[0])[0] + (list1[0])[1] * (list2[1])[0]
new_list1.append(j1)
j2 = (list1[0])[0] * (list2[0])[1] + (list1[0])[1] * (list2[1])[1]
new_list1.append(j2)

j3 = (list1[1])[0] * (list2[0])[0] + (list1[1])[1] * (list2[1])[0] 
new_list2.append(j3)
j4 = (list1[1])[0] * (list2[0])[1] + (list1[1])[1] * (list2[1])[1]
new_list2.append(j4)

new_list = []

new_list.append([new_list1])
new_list.append([new_list2])

print new_list
