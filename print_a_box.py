m = int(raw_input("Width?"))
n = int(raw_input("Height?"))

for i in range(1):
    print "*" * m

for i in range(n-2):
    print "*" + " " * n + "*"

for i in range(1):
    print "*" * m
