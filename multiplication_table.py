#Print the multiplication table for numbers from 1 up to 10.

for j in range(1, 10):
    for i in range(1, 10):
        print str(j) + " X " + str(i) + " = " + str(i*j)
