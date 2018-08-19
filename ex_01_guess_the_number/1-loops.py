from random import randint

steps_counter = 0

rand = randint(0, 100)

while True : # Main loop.
    steps_counter += 1

    while True : # Loop for the user input and checks if valid.
        user_input = input("Input a number between 0 and 100 : ")
        if user_input.isdigit() and int(user_input) < 100 :
            break # We break this loop to return to the main loop.
        print("The input must be a number between 0 and 100. Try again...")
    
    user_input = int(user_input) # Python is dynamicaly typed.

    if user_input == rand :
        break # End the game.
    if user_input > rand :
        print("It's smaller.")
    else :
        print("It's bigger.")

print("\n\n\nWELL DONE !\nThe number was : " + str(rand) + "\nYou guessed it in " + str(steps_counter) + " steps.")
input()
        

    
