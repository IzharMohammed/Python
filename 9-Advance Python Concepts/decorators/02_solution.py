def debug(func):
    """
    Decorator that prints function call details before execution.
    
    Args:
        func: The function to be decorated
    Returns:
        A wrapped version of the function that logs call information
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that handles the logging and function execution.
        
        Args:
            *args: Positional arguments passed to the function
            **kwargs: Keyword arguments passed to the function
        Returns:
            The result of the original function
        """
        # Convert positional arguments to a string
        args_value = ', '.join(str(arg) for arg in args)
        
        # Convert keyword arguments to a string (key=value format)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        
        # Print the function call information
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        
        # Call and return the original function
        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}")


hello()
# Output:
# calling: hello with args  and kwargs 
# hello

greet("izhar", greeting="kya haal chaal")
# Output:
# calling: greet with args izhar and kwargs greeting = kya haal chaal
# kya haal chaal, izhar

'''
How It Works Step-by-Step
When hello() is called:

The wrapper first prints the call info (no args/kwargs)

Then executes the original hello() function

When greet("izhar", greeting="kya haal chaal") is called:

The wrapper logs:

Positional arg: "izhar"

Keyword arg: greeting="kya haal chaal"

Then executes the original greet() function with these arguments
'''