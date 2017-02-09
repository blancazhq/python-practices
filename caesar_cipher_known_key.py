string_input = raw_input("what's the string?")

string = string_input.lower()

string_to_list = list(string)

length = len(string_to_list)

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_to_list = list(alphabet)

key = int(raw_input("key?"))

for i in range (0, length):
    if string_to_list[i] == " ":
        string_to_list[i] = " "
    elif alphabet_to_list.index(string_to_list[i]) + key <= 25:
        alphabet_new_index = alphabet_to_list.index(string_to_list[i]) + key
        string_to_list[i] = alphabet_to_list[alphabet_new_index]
    else:
        alphabet_new_index = alphabet_to_list.index(string_to_list[i]) + key
        string_to_list[i] = alphabet_to_list[alphabet_new_index-26]

new_string = "".join(string_to_list)
print new_string
