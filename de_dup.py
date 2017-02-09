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
