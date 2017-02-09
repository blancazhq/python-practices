#Given a number, print its factors.
#the computer has to loop through one to n, so it occupies a lot of memories

n = int(raw_input("what's the number?"))

for i in range(1, n):
    if n % i == 0:
        print str(n/i)

print "1"
