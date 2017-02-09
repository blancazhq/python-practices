#Given a word as a string, print the result of extending any long vowels to the length of 5.
#you don't have to use the insert() method, you can use replace() method
#Or you can store each letter in a temporary variable(x) when you loop through each letter, and use "x += 'eeee'" 

string_input = raw_input("what's the string?")

string = string_input.lower()

string_to_list = list(string)

length = len(string_to_list)

for i in range (length):
    if string_to_list[i:i+2] == ["a", "a"]:
        string_to_list.insert(i+2, "aaa")
    if string_to_list[i:i+2] == ["e", "e"]:
        string_to_list.insert(i+2, "eee")
    if string_to_list[i:i+2] == ["i", "i"]:
        string_to_list.insert(i+2, "iii")
    if string_to_list[i:i+2] == ["o", "o"]:
        string_to_list.insert(i+2, "ooo")
    if string_to_list[i:i+2] == ["u", "u"]:
        string_to_list.insert(i+2, "uuu")

new_string = "".join(string_to_list)

print new_string
