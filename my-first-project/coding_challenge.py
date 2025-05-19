"""
Difficulty: Beginner
Topic: Loops, Conditionals

Problem Statement
Write a Python program that prints the numbers from 1 to 100.
But for multiples of 3, print "Fizz" instead of the number,
and for the multiples of 5, print "Buzz".
For numbers which are multiples of both 3 and 5, print "FizzBuzz".
"""

#create a function called fizz_buzz
#make sure that it loops throught 1 - 100
#use floor to check if the number is divisble by 3
#use floor to check if the number is divisble by 5
#use floor to check if the number is divisible by 3 & 5
#else print the number 

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
          print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
fizz_buzz()
