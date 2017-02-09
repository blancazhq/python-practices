#Given a string, print the string reversed.
#The string does not take reverse() method, you have to convert string to a list

string = raw_input("what's the string?")

string_to_list = list(string)

print string_to_list

string_to_list.reverse()

string_rev = "".join(string_to_list)

print string_rev
