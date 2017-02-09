string = raw_input("what's the string?")

string_to_list = list(string)

print string_to_list

string_to_list.reverse()

string_rev = "".join(string_to_list)

print string_rev
