#Given a height and width, input by the user, print a box consisting of * characters as its border. 

m = int(raw_input("Width?"))
n = int(raw_input("Height?"))

for i in range(1):
    print "*" * m

for i in range(n-2):
    print "*" + " " * n + "*"

for i in range(1):
    print "*" * m
