

""""
def removeFunc(list, index):
    #return list.pop(index)
    remove = numbers.pop
    print(remove())
    #print(remove(0))

numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]
def is_mult_of_three(n):
    return n % 3 == 0
    
print(list(filter(is_mult_of_three, numbers)))
"""

def get_odd_numbers(numbers_list):
    return [n for n in numbers_list if n % 2 != 0]  # Keep numbers where remainder is not 0 when divided by 2

numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]
odd_numbers = get_odd_numbers(numbers)

print("Odd numbers:", odd_numbers)