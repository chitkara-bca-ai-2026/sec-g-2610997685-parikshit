# Lab 18 - Recursion Practice Toolkit

# Recursive function to calculate factorial
def find_factorial(val):
    if val == 0 or val == 1:
        return 1
    else:
        return val * find_factorial(val - 1)


# Recursive function to generate Fibonacci series
def get_fibonacci(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    else:
        return get_fibonacci(idx - 1) + get_fibonacci(idx - 2)


# Main program
while True:
    print("\n====================================")
    print("     RECURSION PRACTICE TOOLKIT")
    print("====================================")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    option = input("\nEnter your option (1-3): ")

    if option == '1':
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            print("Factorial of", number, "is:", find_factorial(number))

    elif option == '2':
        count = int(input("Enter number of terms: "))

        if count <= 0:
            print("Please enter a positive number.")
        else:
            fib_list = []

            for step in range(count):
                fib_list.append(get_fibonacci(step))

            print("Fibonacci Series:", fib_list)

    elif option == '3':
        print("Thank you for using the Recursion Practice Toolkit. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
