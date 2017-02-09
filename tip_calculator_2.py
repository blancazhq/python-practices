#Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst.

bill = float(raw_input("Total bill amount?"))
service = raw_input("Level of service?")
people = int(raw_input("Split how many ways?"))

if service == "bad":
    tip = bill *0.1
elif service == "fair":
    tip = bill *0.15
elif service == "good":
    tip = bill *0.2


tip_cal = "Tip amount: $%.2f" % tip
print tip_cal

total = bill + tip
total_cal = "Total amount: $%.2f" % total
print total_cal

amount_per_person = total / people
per_person_cal = "Amount per person: $%.2f" % amount_per_person
print per_person_cal
