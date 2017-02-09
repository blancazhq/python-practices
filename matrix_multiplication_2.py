


'''
x = ""

code_storage = []
def code_finder ():
    global a
    global b
    global c
    if code[0] == 0:
            a = "list1"
    elif code[0] ==1:
            a = "list2"
    if code[1] == 0:
            b = 0
    elif code[1] ==1:
            b = 1
    if code[2] == 0:
            c = 0
    elif code[2] ==1:
            c = 1
    print "(" + a +"[" + str(b) + "])[" + str(c) + "]"
    x = "(" + a +"[" + str(b) + "])[" + str(c) + "]"
    code_storage.append(x)
'''

list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]

new_list = [[0, 0], [0, 0]]



for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        for k in range(0, len(list1)):
            new_list[i][j] += list1[i][k] * list2 [k][j]

print new_list


'''
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
