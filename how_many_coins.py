count = 0
print "You have %d coins" % count

while True:
    question = raw_input("Do you want another?")
    if question == "yes":
        count +=1
        print "You have %d coins" % count
    elif question == "no":
        print "Bye"
        break
    else:
        print "Try again"
