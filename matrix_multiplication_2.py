#Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix.
# To visulized this one, I used python tutor to see among i, j and k, which one change first, and second, and third



list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]

new_list = [[0, 0], [0, 0]]



for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        for k in range(0, len(list1)):
            new_list[i][j] += list1[i][k] * list2 [k][j]

print new_list
