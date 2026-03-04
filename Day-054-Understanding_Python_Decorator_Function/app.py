import time

# This is a decorator function - it takes another function as input
def speed_calc_decorator(func):

    # *args and **kwargs allow it to accept any arguments the original function might take
    def wrapper(*args, **kwargs):

        # Record the current time BEFORE calling the function
        start_time = time.time()

        # Actually call the original function (fast_function or slow_function)
        result = func(*args, **kwargs)

        # Record the current time AFTER the function has finished executing
        end_time = time.time()
        # func.__name__ gets the name of the original function as a string
        print(f"{func.__name__} run speed: {end_time - start_time}s")

        # Return whatever the original function returned (maintaining normal behavior)
        return result

    # Return the wrapper function (this replaces the original function)
    return wrapper


# Apply the decorator to fast_function
# This is equivalent to: fast_function = speed_calc_decorator(fast_function)
@speed_calc_decorator
def fast_function():
    # Loop 1,000,000 times (1 million)
    for i in range(1000000):
        # This is just busy work to make the function take some time
        i * i


# Apply the decorator to slow_function
@speed_calc_decorator
def slow_function():
    # Loop 10,000,000 times (10 million) - 10x more than fast_function
    for i in range(10000000):
        # Same calculation as above, just more iterations
        i * i


# Call the decorated functions
# When we call fast_function(), we're actually calling the wrapper function
# that speed_calc_decorator created
fast_function()

# Similarly, this calls the wrapper function that wraps slow_function
slow_function()