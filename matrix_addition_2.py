#Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.
#this is not a solution for matrix of any size. I guess the solution is similar to the matrix multiplication

list1 = [[1, 3, 4], [2, 4, 8],[1, 2, 3]]
list2 = [[5, 2, 6], [1, 0, 9],[1, 2, 3]]

new_list1 = []
new_list2 = []
new_list3 = []

for k in range(0, len(list1)):
    for i in range(0, len(list1)):
        j = (list1[k])[i] + (list2[k])[i]
        if len(new_list1) < len(list1):
            new_list1.append(j)
        elif len(new_list1) == len(list1) and len(new_list2) < len(list1):
            new_list2.append(j)
        elif len(new_list1) > len(list1) and len(new_list2) < len(list1):
            new_list2.append(j)
        elif len(new_list2) == len(list1):
            new_list3.append(j)
        elif len(new_list2) > len(list1):
            new_list3.append(j)


new_list = []

new_list.append([new_list1])
new_list.append([new_list2])
new_list.append([new_list3])

print new_list
