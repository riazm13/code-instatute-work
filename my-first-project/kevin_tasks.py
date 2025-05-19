"""

1. FizzBuzz

Write some code that iterates the numbers 1 to 100, and does the following:
- If the number is divisible by 3, output "Fizz"
- If the number is divisible by 5, output "Buzz"
- If the number is divisible by 3 and 5, output "FizzBuzz"
- Otherwise, output the number
"""

def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
FizzBuzz()






"""
2. Given the following list of numbers:

[1, 10, 40, 23, 19, 42, 12, 18, 17, 21, 8, 2]

Write a function which takes a number as a parameter, and checks if the
list contains two numbers which add up to that number. If there are, return the two numbers.
If not, return None. For example:

check_list(54)
-> returns [42, 12]

check_list(31)
-> returns [10, 21]

check_list(1000)
-> returns None
"""
def check_list(target_sum):
    numbers = [1, 10, 40, 23, 19, 42, 12, 18, 17, 21, 8, 2]
    seen = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            return [number, complement]
        seen.add(number)
    return None
print(check_list(54))  
print(check_list(31))  
print(check_list(1000))  