def print_it(func):
    def wrapper(*args, **kwargs):
        # print out the arguments and keyword arguments
        print(f'Arguments: {args}')
        print(f'Keyword Arguments:  {kwargs}')
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Print the result
        print(f'Result: {result}')
        
        return result
    return wrapper

@print_it
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(1, 2))





numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]



