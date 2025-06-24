import time  # Import the time module for time measurement functions

# Define a decorator function called 'timer'
def timer(func):
    """
    Decorator that measures and prints the execution time of the wrapped function.
    
    Args:
        func: The function to be timed
    Returns:
        A wrapped version of the function that includes timing functionality
    """
    def wrapper(*args, **kwargs):
        """
        The wrapper function that adds timing functionality around the original function.
        
        Args:
            *args: Positional arguments passed to the original function
            **kwargs: Keyword arguments passed to the original function
        Returns:
            The result of the original function
        """
        start = time.time()  # Record the start time
        
        # Call the original function with its arguments and store the result
        result = func(*args, **kwargs)
        
        end = time.time()  # Record the end time
        
        # Print the function name and execution duration
        print(f"{func.__name__} ran in {end-start} seconds")
        
        return result  # Return the original function's result
    
    return wrapper  # Return the wrapper function


# Apply the @timer decorator to example_function
@timer
def example_function(n):
    """
    Example function that sleeps for 'n' seconds to demonstrate the timer decorator.
    
    Args:
        n: Number of seconds to sleep
    """
    time.sleep(n)  # Pause execution for 'n' seconds


# Call the decorated function
example_function(2)


'''
Decorator Application (@timer):

The @timer syntax is equivalent to:

example_function = timer(example_function)
'''