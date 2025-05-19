"""
Difficulty: Beginner
Topics: Strings, Functions, Conditionals

Problem Statement
Write a function called is_palindrome that checks whether a given string is a palindrome.

A palindrome is a word, phrase, or number that reads the same backward as forward.
Ignore spaces, punctuation, and letter casing.

Function Signature
python
Copy
Edit
def is_palindrome(text: str) -> bool:
Example Input & Output
python
Copy
Edit
is_palindrome("Racecar")       # True  
is_palindrome("hello")         # False  
is_palindrome("A man a plan a canal Panama")  # True  
✅ Bonus Task:
Make it work for full sentences with spaces and mixed case.

Use .lower() and string manipulation to ignore spaces.
"""

# need to check if the string is the same when reversed
# will output  True if it is a palindrome
# will output False if it is not a palindrome
#remove spaces and punctuation
#add the string to a list

def is_palindrome(text: str) -> bool:
    clean_string = ''.join(char.lower() for char in text if char.isalnum())
    return clean_string == clean_string[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("penis"))
