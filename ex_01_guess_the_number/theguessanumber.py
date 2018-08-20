from random import randint

a = int(input("Pick a number from 0 to 100"))

random = randint(0,100)

if a > random:
    print("Lower")
elif a < random:
    print("Higher")
else:
    print("You win ha")
