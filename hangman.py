import os

wrong_counter = 0
right_handler = False
letter = ""

def draw_rack():
    print "+--------+"
    print "|        |"
    for i in range(0, 7):
        print "|"
    print "----------"

def draw_hangman_1():
    print "+--------+"
    print "|        |"
    print "|        O"
    for i in range(0, 6):
        print "|"
    print "----------"

def draw_hangman_2():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|        |"
    for i in range(0, 5):
        print "|"
    print "----------"

def draw_hangman_3():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|"
    for i in range(0, 5):
        print "|"
    print "----------"

def draw_hangman_4():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|\\"
    for i in range(0, 5):
        print "|"
    print "----------"

def draw_hangman_5():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|\\"
    print "|       /"
    for i in range(0, 4):
        print "|"
    print "----------"

def draw_hangman_6():
    print "+--------+"
    print "|        |"
    print "|        O"
    print "|       /|\\"
    print "|       / \\"
    for i in range(0, 4):
        print "|"
    print "----------"
    print "Game Over!"


def check_right():
    for i in range(0, len(word_to_list)):
        global letter
        if letter == word_to_list[i]:
            new_list[i] = letter
            global right_handler
            right_handler = True



draw_rack()

secret_word = "apple"

word_to_list = list(secret_word)

new_list = []

for i in range(0, len(word_to_list)):
    new_list.append("_")

new_string = " ".join(new_list)
print new_string

while True:

    if "".join(new_list) == secret_word:
        print "You win!"
        break

    right_handler = False

    letter = raw_input("guess a letter?")

    check_right()

    new_string = " ".join(new_list)
    print new_string

    if right_handler == False:
        os.system("clear")
        wrong_counter += 1
        if wrong_counter == 1:
            print new_string
            draw_hangman_1()
        elif wrong_counter == 2:
            print new_string
            draw_hangman_2()
        elif wrong_counter == 3:
            print new_string
            draw_hangman_3()
        elif wrong_counter == 4:
            print new_string
            draw_hangman_4()
        elif wrong_counter == 5:
            print new_string
            draw_hangman_5()
        elif wrong_counter == 6:
            print new_string
            draw_hangman_6()
            break
