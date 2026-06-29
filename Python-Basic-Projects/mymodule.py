'''
Q8. (Custom Module)
Create a custom module file named mymodule.py that contains:
A function greet(name) that prints "Hello [name], Welcome to Python Class!"
A function calculate_power(base, exp) that returns base raised to exponent.
Then write a main program that imports this module and uses both functions.
'''

# Function to print a welcome message
def greet(name):
    print(f"Hello {name}, Welcome to Python Class!")


# Function to calculate and return the power value
def calculate_power(base, exp):
    res = base**exp
    return res


'''
Q9. (name == "main")
Write a program that:
a) Creates a small function and demonstrates the use of if __name__ ==
"__main__": so that some code runs only when the file is executed directly.
'''

#Running Test Code Inside Module
if __name__ == "__main__":
    # This code ONLY runs if you open "mymodule.py" and click play.
    # It will be completely IGNORED if another file imports this script.
    print("Testing the greet function:")
    print(greet("Omkar"))

    print("\nTesting calculate_power(4,7):", calculate_power(4,7))