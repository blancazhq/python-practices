import random

play_again_handler = True

def generate():

    global play_again_handler

    password_list = []
    digit_counter = 0
    play_again_handler = True

    while True:
        input_message = raw_input("how strong do you want your password to be?(strong/medium/weak)")
        if input_message == "strong":
            digit_counter = random.choice(range(13, 21))
            break
        elif input_message == "medium":
            digit_counter = random.choice(range(7, 13))
            break
        elif input_message == "weak":
            digit_counter = random.choice(range(3, 7))
            break
        else:
            print "Say something that makes sense to me..."
            continue


    symbol_list = range(33, 48)+range(63, 65)+range(91, 97)+range(126, 127)
    number_list = range(48, 57)
    upper_list = range(65, 91)
    lower_list = range(97, 123)

    for i in range(0, digit_counter+1):

        if input_message == "strong":
            password_list.append(chr(random.choice(symbol_list+number_list+upper_list+lower_list)))
        elif input_message == "medium":
            password_list.append(chr(random.choice(number_list+upper_list+lower_list)))
        elif input_message == "weak":
            password_list.append(chr(random.choice(lower_list)))

    password_string = "".join(password_list)

    print "Your password is " +password_string

    while True:
        play_again_message = raw_input("wanna do it again?(y/n)")
        if play_again_message == "y":
            break
        elif play_again_message == "n":
            play_again_handler = False
            break
        else:
            continue

while True:
    if play_again_handler == True:
        generate()
    if play_again_handler == False:
        print "Bye!"
        break
