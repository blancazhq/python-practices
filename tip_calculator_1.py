'''
Prompt the user for two things:

The total bill amount
The level of service, which can be one of the following: good, fair, or bad
Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

good -> 20%
fair -> 15%
bad -> 10%

bill = float(raw_input("Total bill amount?"))
service = raw_input("Level of service?")
'''


if service == "bad":
    tip = bill *0.1
elif service == "fair":
    tip = bill *0.15
elif service == "good":
    tip = bill *0.2


tip_cal = "Tip amount: $%.2f" % tip
print tip_cal
