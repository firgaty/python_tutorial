from random import randint

def menu () : # Level selector.
    while True :
        print("Choose the upper bound :\n1) 100\n2) 1000\n3) 10000\nEnter 1, 2 or 3 :")
        user_input = input()

        if user_input.isdigit() :
            if int(user_input) == 1 :
                return 100, 0
            elif int(user_input) == 2 :
                return 1000, 1
            elif int(user_input) == 3 :
                return 10000, 2

        print("Wrong input.")

def get_user_input(upper_bound) :
    while True:  # Loop for the user input and checks if valid.
        user_input = input("Input a number between 0 and "+ str(upper_bound) + " : ")

        if user_input == "DEV_MOD" : # For dev purpose it will serve as an 'always true' statement.
            return -1
        
        if user_input.isdigit() and int(user_input) < upper_bound:
            return int(user_input)  # Python is dynamicaly typed.
        
        print("The input must be a number between 0 and 100. Try again...")

    
        
def game () : # Game loop
    steps_counter = 0
    upper_bound, size = menu()
    rand = randint(0, upper_bound)

    while True:  # Main loop.
        steps_counter += 1

        user_input = get_user_input(upper_bound)

        if user_input == -1 : # Dev usage.
            steps_counter += randint(0, 7)
            break

        if user_input == rand :
            break  # End the game.
        if user_input > rand :
            print("It's smaller.")
        else:
            print("It's bigger.")

    print("\n\n\nWELL DONE !\nThe number was : " + str(rand) +
          "\nYou guessed it in " + str(steps_counter) + " steps.\n")
    input()
        
    return steps_counter, size

def get_yes_no_input() : # Self Explicit
    while True :
        user_input = input("(Y)es/(N)o ? : ")

        # Here I cheat a little by using a Set. I could have used a list for the same purpose.
        if user_input in {"Yes", "yes" "y", "Y", ""} :
            return True
        elif user_input in {"No", "no", "N", "n"} : # And there too.
            return False

def print_scores_list(scores_list) :
    print("-----------------------\nYour best scores are : ")

    for i in range(len(scores_list)) :
        print(str(10 ** (i + 2)) + " : " + (str(scores_list[i]) if not scores_list[i] == None else "N/A"))
                                            # ^        This is a ternary operator equivalent           ^
                                            #    (return_this) if (my_condition) else (return_else_this)
                                            # It's like an inline if/else.
    input()

#####################
### Main function ###
#####################

def main() :
    print("Welcome !")

    min_counter = [None] * 3

    while True :
        counter, size = game() # I get the 2 vars that gmae() returned.
        if min_counter[size] is None or counter[size] < min_counter :
            min_counter[size] = counter
        
        print_scores_list(min_counter)

        print("\n\n\nDo you want to start a new game ?")
        if not get_yes_no_input() :
            print("Good Bye !")
            break


# This part tell Python : 'If you launched this file, call the main() function.
# But if this file was imported, do not.
if __name__ == "__main__" :
    main()
