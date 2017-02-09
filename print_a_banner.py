#Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. 

text = raw_input("Text?")
length = len(text)

for i in range(1):
    print "*" * (length + 4)

for i in range(1):
    print "*" + " " + text + " " + "*"

for i in range(1):
    print "*" * (length + 4)
