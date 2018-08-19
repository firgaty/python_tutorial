# Exercise 01 : Guess the number

## Goal

Write a Python program with which we can play the guess the number game.

## Rules

1) The computer chooses a number in a range (at first between 1 and 100).
2) The computer asks the player what the number is.
3) The player inputs a number.
4) The computer checks if what's entered is correct, if not it goes back to step (2)
5) The computer tells the player that the player won.

## What you need

- A random function, Python has one.

```python
from random import randint

rand_nb = randint(a,b) # a and b are the boundaries.
```
- A function to get the player input.
  
```python
player_input = input("My message")
```

It will print the message and wait for an input from the player. This function will return a `'str'` type object.

- A function to get an integer from a string.

```python
my_int = int(my_str)
```