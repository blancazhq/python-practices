def checker():
    global game_record
    global player_a_name
    global player_b_name
    global checker_handler

    a = game_record.replace(" ", "")
    b = a.replace("-", "")
    c = b.replace("\n", "")
    game_data = c.replace("|", "")

    if game_data[0] == game_data[1] ==  game_data[2] or game_data[3] == game_data[4] ==  game_data[5] or game_data[6] == game_data[7] ==  game_data[8] or game_data[0] == game_data[3] ==  game_data[6] or game_data[1] == game_data[4] ==  game_data[7] or game_data[2] == game_data[5] ==  game_data[8] or game_data[0] == game_data[4] ==  game_data[8] or game_data[2] == game_data[4] ==  game_data[6]:
        checker_handler = True
        if game_data[0] == game_data[1] ==  game_data[2] == "x" or game_data[3] == game_data[4] == game_data[5] == "x" or game_data[6] == game_data[7] ==  game_data[8] == "x" or game_data[0] == game_data[3] ==  game_data[6]  == "x" or game_data[1] == game_data[4] ==  game_data[7]  == "x" or game_data[2] == game_data[5] ==  game_data[8] == "x" or game_data[0] == game_data[4] ==  game_data[8]  == "x"or game_data[2] == game_data[4] ==  game_data[6] == "x":
            winner = player_a_name
        else:
            winner = player_b_name
        print "The winner is " + winner + "! Congratulations!"

def playagain ():
    global play_again_handler
    while True:
        play_again = raw_input("Do you want to play again?(y or n)")
        if play_again == "n":
            play_again_handler = False
            break
        elif play_again == "y":
            break
        else:
            continue


location = "--- --- ---\n 1 | 2 | 3\n--- --- ---\n 4 | 5 | 6\n--- --- ---\n 7 | 8 | 9\n--- --- ---\n"
round_counter = 0
checker_handler = False
game_record = location
play_again_handler = True
runner = True

def game():
    global location
    global round_counter
    global game_record
    global player_a_name
    global player_b_name
    global checker_handler
    global play_again_handler
    global runner

    round_counter = 0
    checker_handler = False
    game_record = location
    play_again_handler = True
    runner = True


    print "\nTIC - TAC - TOE\n"
    print location

    player_a_name = raw_input("If you want to go first, tell me your name?")

    print "\nwelcome, " + player_a_name + "!\n"

    player_b_name = raw_input("what's your name?")

    print "\nwelcome, " + player_b_name + "!\n"

    print location

    while runner == True:


        while runner == True:
            player_a_input = raw_input(player_a_name + ", what location do you want to draw an O?")
            game_record = game_record.replace(player_a_input, "O")
            round_counter += 1
            print game_record
            checker()
            if checker_handler == True:
                playagain()
                runner = False
                break
            break

        while runner == True:
            player_b_input = raw_input(player_b_name + ", what location do you want to draw an x?")
            game_record = game_record.replace(player_b_input, "x")
            round_counter += 1
            print game_record
            checker()
            if checker_handler == True:
                playagain()
                runner = False
                break
            break

        while runner == True:
            if round_counter >= 9:
                print " \nGame Over!"
            if checker_handler == True:
                playagain()
                runner = False
                break
            break

while True:
    if play_again_handler == True:
        game()
    if play_again_handler == False:
        print "Bye!"
        break
