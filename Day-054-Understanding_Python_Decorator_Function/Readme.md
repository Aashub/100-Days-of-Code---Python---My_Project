# Day 54 – Exercise: Understanding Python Decorator Function

## Exercise Overview

This Exercise is a Python-based exploration of decorators and higher-order functions through a practical function timing application. The script demonstrates how decorators work by creating a speed_calc_decorator that measures the execution time of any function it wraps. Two functions (fast_function and slow_function) perform mathematical operations with different loop iterations, and the decorator automatically calculates and displays their execution times. The main goal of this Day was to understand advanced Python concepts including decorators, nested functions, function wrapping, and @syntax, _name_ and _main_ special attributes and also how to use command line.

## What I Have Learned

* **Command Line Python**: Learned essential command line operations such as how to create new directories using `mkdir`, create new files with `touch` or type `nul`, navigate into directories with `cd`, move back to parent directory using `cd ..`, delete files with `rm or del`, and remove directories with `rmdir or rm -rf`. 
* **Python Decorators**: learned how to create decorators & Understood how decorators are special functions that modify the behavior of other functions without changing their source code
* **Functions as Arguments**: Learned that functions can be passed as arguments to other functions and returned as values from functions
* **Returning Functions**: Understood how a function can create and return another function (like the wrapper returning from speed_calc_decorator)
* **__name__ and __main__ Special Attributes**: __name__: Learned that every Python module has a built-in __name__ attribute. When a module is run directly, __name__ is set to "__main__". When a module is imported into another script, __name__ is set to the module's filename (without .py). This allows modules to determine whether they're being run as the main program or being used as an imported module.

## What I Have Learned

* **Decorator Definition**: The speed_calc_decorator function is defined as a decorator that takes another function (func) as its input. This is the foundation of the decorator pattern - a function that accepts a function and returns a modified version of it.
* **Nested Wrapper Function**: Inside the decorator, a nested function called wrapper is defined. This wrapper function accepts any arguments using *args and **kwargs syntax, which allows the decorator to work with any function regardless of what parameters it takes. The wrapper contains the additional timing logic that will be added to the original function.
* **Timing Logic Implementation**: The wrapper function records the start time using time.time() before doing anything else. It then calls the original function (func) with whatever arguments were passed in (*args, **kwargs) and stores the result. After the function completes, it records the end time and calculates the difference. It then prints the function name (using func.__name__) along with the calculated execution time in seconds.
* **Decorator Return Value**: The decorator returns the wrapper function (without calling it). This is crucial - the decorator replaces the original function with this new wrapper function that contains the timing logic plus the original functionality.
* **Function Decoration**: The @speed_calc_decorator syntax is applied to both fast_function and slow_function. This is syntactic sugar that effectively does fast_function = speed_calc_decorator(fast_function) and slow_function = speed_calc_decorator(slow_function). After this, whenever these functions are called, they actually call the wrapper function instead.
* **Function Execution**: When fast_function() and slow_function() are called at the end of the script, they execute their loops while the decorator automatically times them and prints the results, demonstrating how decorators can add functionality without modifying the original function code.

## Project Highlights

* Learned how to create and apply decorators using @ syntax to add functionality (timing) to existing functions without modifying their code
* Understood that functions can accept other functions as arguments and return new functions as results
* learned creating functions inside functions and how inner functions retain access to outer function variables
* Learned about command line and how to use them in navigating, creating, and deleting files/directories through terminal commands like mkdir, cd, touch, and rm.
* Understood how the __name__ attribute helps distinguish between running a script directly (__main__) versus importing it as a module (filename), enabling flexible code execution

