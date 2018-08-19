from random import randint

def menu () : # Level selector.
    while True :
        print("Choose the upper bound :\n1) 100\n2) 1000\n3) 10000\nEnter 1, 2 or 3 :")
        user_input = input()

        if user_input.isdigit() :
            if int(user_input) == 1 :
                return 100
            elif int(user_input) == 2 :
                return 1000
            elif int(user_input) == 3 :
                return 10000

        print("Wrong input.")

def get_user_input(upper_bound) :
    while True:  # Loop for the user input and checks if valid.
        user_input = input("Input a number between 0 and "+ str(upper_bound) + " : ")
        if user_input.isdigit() and int(user_input) < upper_bound:
            break  # We break this loop to return to the main loop.
        print("The input must be a number between 0 and 100. Try again...")

    return int(user_input)  # Python is dynamicaly typed.
        
def game () : # Game loop
    steps_counter = 0
    upper_bound = menu()
    rand = randint(0, upper_bound)

    while True:  # Main loop.
        steps_counter += 1

        user_input = get_user_input(upper_bound)

        if user_input == rand:
            break  # End the game.
        if user_input > rand:
            print("It's smaller.")
        else:
            print("It's bigger.")

    print("\n\n\nWELL DONE !\nThe number was : " + str(rand) +
          "\nYou guessed it in " + str(steps_counter) + " steps.")
        
    return steps_counter

def get_yes_no_input() : # Self Explicit
    while True :
        user_input = input("(Y)es/(N)o ? : ")
        if user_input in {"Yes", "yes" "y", "Y", ""} : # Here I cheat a little by using lists.
            return True
        elif user_input in {"No", "no", "N", "n"} : # And there too.
            return False

def main() :
    print("Welcome !")

    min_counter = None
    while True :
        counter = game()
        if min_counter is None or counter < min_counter :
            min_counter = counter
        
        print("Your best score in this session is : " + str(min_counter) + " steps.")
        input()
        print("\n\n\nDo you want to start a new game ?")
        if not get_yes_no_input() :
            print("Good Bye !")
            break


if __name__ == "__main__" :
    main()
