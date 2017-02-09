#Prompt the user for his name using the raw_input function.
#Upon receiving his name, you will say hello to him.
#make your greeting all cap.

name = raw_input("what's your name?")
string1 = "Hello, %s!" % name
string2 = "Your name has %d letters in it! Awesome!" % len(name)

print string1.upper()

print string2.upper()
