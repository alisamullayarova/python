def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapper

@validate_args
def example_function(arg):
    return f"The argument {arg} is valid."

print(example_function(5))  
print(example_function())   
print(example_function(1, 2)) 
print(example_function("xx"))  
print(example_function(-3))    