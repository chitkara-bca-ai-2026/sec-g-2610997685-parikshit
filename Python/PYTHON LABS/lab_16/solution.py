def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2


def remainder(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 % num2


def exponent(num1, num2):
    return num1 ** num2


def convert_c_to_f(temp_c):
    return (temp_c * 9/5) + 32


def show_history(calc_history):
    print("\n--- Calculation Log ---")
    if not calc_history:
        print("No history available.")
    else:
        for entry in calc_history:
            print(entry)


def run_calculator():
    calc_history = []

    while True:
        print("\n====================================")
        print("         MATH TOOLKIT PRO")
        print("====================================")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Temperature Conversion")
        print("8. View History")
        print("9. Exit")
        print("====================================")

        try:
            option = int(input("Enter your option (1-9): "))

            if option == 9:
                answer = input("Are you sure you want to exit? (y/n): ")
                if answer.lower() == 'y':
                    print("Thank you for using Math Toolkit Pro!")
                    break
                else:
                    continue

            elif option == 8:
                show_history(calc_history)

            elif option == 7:
                temp_c = float(input("Enter temperature in Celsius: "))
                output = convert_c_to_f(temp_c)
                print("Temperature in Fahrenheit:", output)
                calc_history.append(f"{temp_c} Celsius = {output} Fahrenheit")

            elif option in:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if option == 1:
                    output = addition(num1, num2)
                    symbol = "+"

                elif option == 2:
                    output = subtraction(num1, num2)
                    symbol = "-"

                elif option == 3:
                    output = multiplication(num1, num2)
                    symbol = "*"

                elif option == 4:
                    output = division(num1, num2)
                    symbol = "/"

                elif option == 5:
                    output = remainder(num1, num2)
                    symbol = "%"

                elif option == 6:
                    output = exponent(num1, num2)
                    symbol = "**"

                print("Result:", output)

                if not isinstance(output, str):
                    calc_history.append(f"{num1} {symbol} {num2} = {output}")

            else:
                print("Invalid choice! Please select between 1 and 9.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        except Exception as err:
            print("An error occurred:", err)


if __name__ == "__main__":
    run_calculator()
