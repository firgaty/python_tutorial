# INTRODUCTION

## First things first...

To get something right, you must begin somewhere. And _this_ somewhere has to be suitable and the best thing to begin at.

```python
print("Hello world!")
```

Yes, this is **it**."Hello World!", the program that starts everything. It allows us to see if you have python installed correctly, up and running, and to get you in a nice mood. It's amazing.

## What we'll do

As for any language, we'll need to do things in a certain order and it will be set by... well... myself. **BUT** you may always ask me about things unrelated to any chapter that we'll do and we'll see how it goes.

Here's how I think we'll proceed :
  
- Command line interpreter
- Basic Operations
- Caracter sets
- if / else / elif
- while loop
- for loop
- Lists
- functions
- Strings
- class
- Object Oriented Programming
- ... to be updated.

Of course, if you've already covered a few of the items in this list, we'll just skim over it.

Now, let's move on to the first part.

# Command line interpreter

Here I'm going to discuss how useful the command line interpreteur, or **CLI** is.

It's often considered as useless for beginner developpers because all the code you write will be erased from your computer memory at the moment you'll exit the CLI you were typing it in. So a lot of inexperienced python devs were brought to the edge of their patience while using this amazing tool thus resulting in a complete reject of it.

While I don't use it often, it saved me quite a lot of effort testing minor ideas I have on my mind. So, you may not like it, but sometimes it'll just pop in your head that it **is** a useful tool. And so, for our sake, we'll start with it to get the hang of python's operations and core logic and then we'll move on to writing scripts.

> Now, how do we open this CLI ?

To do so, open your terminal and type `python`.

Here you go.

Now you'll have something like:

```
Python 3.6.6 (default, Jun 27 2018, 13:11:40) 
[GCC 8.1.1 20180531] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Now, within this CLI, are able to do a lot of things. Actually, everything you're able to do in python can be done with this command line tool... If you have patiente and courage.

But, thanks to this tool we'll test a few things.

# Basic Operations

## Arithmetic Operators

In python, there's a set of operators, some common to other languages, others not quite so. They go as follows :

|Sign|Name|Comments|
|-|-|-|
| + | Addition | Regular Addition. |
| - | Substraction | Regular Substraction. |
| * | Multiplication | Regular Multiplication. |
| / | Division | Regular division. |
| ** | Exponant | When you want to use an exponant : 2 ** 8  is  $2^3$ which is 8.
| % | Modulo | Modulo is the "remainder" of an Euclidean division : 10 % 3 is $10 \bmod [2]$ which is 1 | 
| // | Floor Division | Gives us the quotient of an Euclidean division : 10 // 3 is 3. |

Also, python language follows the regular algebraic rules to evaluate expression. That means that the addition and substraction are of the same importance, inferior to the multiplication, division, modulo and floor division which in turn are inferior to exponants and parentheses.

This turns python, and the CLI, into a powerful calculator.

## Comparison Operators

Often, you'll need to compare two values. And these are the operators associated to comparing values.

| Operator | Description | Example |
|-|-|-|
|==| If the values of two operands are equal, then the condition becomes true.|(a == b) is not true.|
|!=| If values of two operands are not equal, then condition becomes true.|(a != b) is true.|
|<>| If values of two operands are not equal, then condition becomes true.|(a <> b) is true. This is similar to != operator.|
|>| If the value of left operand is greater than the value of right operand, then condition becomes true.| (a > b) is not true.|
|<| If the value of left operand is less than the value of right operand, then condition becomes true.|(a < b) is true.|
|>=| If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.|(a >= b) is not true.|
|<=| If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|(a <= b) is true.|

# TODO

# Conditions

## if

The `if` block is executed only IF the condition is met. That means the condition, at it's evaluation, must be `True`.

![alt text](diagrams/if_block_dia_alpha.png "if")

In python, it's writen as follows :

```python
if myCondition :
    myInstructionInTheIfBlock
```

## else

The `else` block is executed IF the condition in the `if` statement evaluates to `False`.