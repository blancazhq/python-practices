#Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. 

n = int(raw_input("Start from: "))
m = int(raw_input("Ends on: "))
for i in range(n, m + 1):
    print i
