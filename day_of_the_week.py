#Given the following code that prompts the user for a day number

day = int(raw_input("Day(0-6?)"))

if day == 0:
    print "Sunday"
elif day == 1:
    print "Monday"
elif day == 2:
    print "Tueday"
elif day == 3:
    print "Wednesday"
elif day == 4:
    print "Thursday"
elif day == 5:
    print "Friday"
elif day == 6:
    print "Saturday"
else:
    print "not a valid number!"
