#Given a number, print its factors.
#the computer has to loop through one to n, so it occupies a lot of memories

n = int(raw_input("what's the number?"))

new_list = []

for i in range(1, n):
    if n % i == 0:
        new_list.append(n/i)

new_list_2 = new_list.reverse()

new_list_3 = []

prime = True

for j in range(0, len(new_list)):
    for k in range(0, j):
        if new_list[j] % new_list[k] == 0:
            prime = False
    if prime == True:
        new_list_3.append(new_list[j])

print new_list_3
