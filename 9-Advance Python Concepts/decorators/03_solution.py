import time

def cache(func):
    """
    Decorator that caches function results to avoid recomputation.
    
    Maintains a dictionary where:
    - Keys are function argument tuples
    - Values are corresponding return values
    """
    cache_value = {}  # Dictionary to store cached results
    print(cache_value)  # Prints initial empty cache (runs when decorator is applied)
    
    def wrapper(*args):
        """
        Wrapper function that checks cache before executing the function.
        
        Args:
            *args: Positional arguments to the function
        Returns:
            Cached result if available, otherwise newly computed result
        """
        if args in cache_value:  # Check if result is cached
            return cache_value[args]
        
        result = func(*args)  # Compute result if not cached
        cache_value[args] = result  # Store result in cache
        return result
    
    return wrapper

@cache
def long_running_function(a, b):
    """
    Simulates an expensive computation by sleeping for 4 seconds.
    
    Args:
        a: First number
        b: Second number
    Returns:
        Sum of a and b
    """
    time.sleep(4)  # Simulate long computation
    return a + b


print(long_running_function(2, 3))  # Takes ~4 seconds
print(long_running_function(2, 3))  # Returns immediately (cached)
print(long_running_function(4, 3))  # Takes ~4 seconds (new args)

'''
output:-
{}  # Printed when decorator is applied (empty initial cache)
5   # First call (takes 4 seconds)
5   # Second call (instant from cache)
7   # Third call (takes 4 seconds)
'''

'''
How It Works Step-by-Step
First Call long_running_function(2, 3):

Cache is empty ({})

Executes the slow computation (4 seconds)

Stores result: {(2, 3): 5}

Returns 5

Second Call long_running_function(2, 3):

Finds (2, 3) in cache

Immediately returns cached value 5

Third Call long_running_function(4, 3):

New arguments not in cache

Executes slow computation (4 seconds)

Stores result: {(2, 3): 5, (4, 3): 7}

Returns 7
'''