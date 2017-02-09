import random

play_again = "Y"

while True:
    if play_again == "Y":

        secret_number = random.randint(1, 10)

        print "I'm thinking of a number between 1 and 10."

        count = 5

        while True:
            print "You have %d guesses left." % count

            while true:
                try:
                    number_input = int(raw_input("What's the number?"))
                    break
                except ValueError:
                    print "That's not a number"

            if number_input > secret_number:
                print "%d is too high" % number_input
                count -= 1
            elif number_input < secret_number:
                print "%d is too low" % number_input
                count -= 1
            elif number_input == secret_number:
                print "Yes! You win!"
                play_agian = raw_input("Do you want to play again (Y or N)?")
                break

            if count < 1:
                print "You ran out of guesses"
                play_again = raw_input("Do you want to play again (Y or N)?")
                break
    elif play_again == "N":
        print "Bye"
        break
    else:
        print "try again"
        play_again = raw_input("Do you want to play again (Y or N)?")
