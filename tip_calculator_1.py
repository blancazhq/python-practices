bill = float(raw_input("Total bill amount?"))
service = raw_input("Level of service?")


if service == "bad":
    tip = bill *0.1
elif service == "fair":
    tip = bill *0.15
elif service == "good":
    tip = bill *0.2


tip_cal = "Tip amount: $%.2f" % tip
print tip_cal
