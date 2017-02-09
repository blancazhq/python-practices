#Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.

n = int(raw_input("height?"))

for i in range(n):
    print " " * (n-1-i) + "*" * (2*i+1)
