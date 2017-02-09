text = raw_input("Text?")
length = len(text)

for i in range(1):
    print "*" * (length + 4)

for i in range(1):
    print "*" + " " + text + " " + "*"

for i in range(1):
    print "*" * (length + 4)
