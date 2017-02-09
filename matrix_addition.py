#Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists,
#Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.
#You don't have to use "(list1[0])[0]", you can use "list1[0][0]"

list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]

new_list1 = []
new_list2 = []

for i in range(0, len(list1)):
        j = (list1[0])[i] + (list2[0])[i]
        new_list1.append(j)

for i in range(0, len(list1)):
        j = (list1[1])[i] + (list2[1])[i]
        new_list2.append(j)

new_list = []

new_list.append([new_list1])
new_list.append([new_list2])

print new_list
