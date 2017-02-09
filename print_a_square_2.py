#Print a NxN square of * characters. Prompt the user for N. 

n = int(raw_input("How big is the square?"))

for i in range(n):
    print "*" * n
