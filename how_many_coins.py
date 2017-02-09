#Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. 

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
