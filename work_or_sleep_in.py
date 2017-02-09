#Prompt the user for a day of the week just like the previous problem. Except this time print "Go to work" if it's a work day and "Sleep in" if it's a weekend day.

day = int(raw_input("Day(0-6?)"))

if day == 0:
    print "Sleep in"
elif day == 1:
    print "Work"
elif day == 2:
    print "Work"
elif day == 3:
    print "Work"
elif day == 4:
    print "Work"
elif day == 5:
    print "Work"
elif day == 6:
    print "Work"
else:
    print "not a valid number!"
