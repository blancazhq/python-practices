#Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase)
# you can also use string.replace(old, new) method

string_input = raw_input("what's the string?")

string = string_input.upper()

string_to_list = list(string)

length = len(string_to_list)

for i in range (0, length):
    if string_to_list[i] == "A":
        string_to_list[i] = "4"
    if string_to_list[i] == "E":
        string_to_list[i] = "3"
    if string_to_list[i] == "G":
        string_to_list[i] = "6"
    if string_to_list[i] == "I":
        string_to_list[i] = "1"
    if string_to_list[i] == "O":
        string_to_list[i] = "0"
    if string_to_list[i] == "S":
        string_to_list[i] = "5"
    if string_to_list[i] == "T":
        string_to_list[i] = "7"

new_string = "".join(string_to_list)

print new_string
