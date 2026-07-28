import math
from datetime import datetime

HISTORY_FILE = "history.txt"


def log_history(text):
    """Save each calculation to history.txt with date and time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {text}\n"
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(line)


def show_menu():
    print("\n" + "=" * 40)
    print("      PROFESSIONAL CALCULATOR")
    print("=" * 40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Average")
    print("9. Factorial")
    print("10. Sum Unlimited Numbers")
    print("11. Show History")
    print("12. Exit")
    print("=" * 40)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def add_numbers():
    count = get_int("How many numbers do you want to add? ")
    if count <= 0:
        print("Number must be greater than 0.")
        return

    numbers = []
    for i in range(count):
        num = get_float(f"Enter number {i + 1}: ")
        numbers.append(num)

    result = sum(numbers)
    expression = " + ".join(str(n) for n in numbers)
    print(f"Result: {result}")
    log_history(f"{expression} = {result}")


def subtract_numbers():
    num1 = get_float("Enter first number: ")
    num2 = get_float("Enter second number: ")
    result = num1 - num2
    print(f"Result: {result}")
    log_history(f"{num1} - {num2} = {result}")


def multiply_numbers():
    count = get_int("How many numbers do you want to multiply? ")
    if count <= 0:
        print("Number must be greater than 0.")
        return

    result = 1
    numbers = []

    for i in range(count):
        num = get_float(f"Enter number {i + 1}: ")
        numbers.append(num)
        result *= num

    expression = " × ".join(str(n) for n in numbers)
    print(f"Result: {result}")
    log_history(f"{expression} = {result}")


def divide_numbers():
    num1 = get_float("Enter first number: ")
    num2 = get_float("Enter second number: ")

    if num2 == 0:
        print("Error: Cannot divide by zero.")
        log_history(f"{num1} / {num2} = Error (division by zero)")
        return

    result = num1 / num2
    print(f"Result: {result}")
    log_history(f"{num1} / {num2} = {result}")


def power_numbers():
    base = get_float("Enter base: ")
    exponent = get_float("Enter exponent: ")
    result = math.pow(base, exponent)
    print(f"Result: {result}")
    log_history(f"{base} ^ {exponent} = {result}")


def square_root():
    num = get_float("Enter number: ")

    if num < 0:
        print("Error: Square root of negative numbers is not allowed.")
        log_history(f"√{num} = Error (negative number)")
        return

    result = math.sqrt(num)
    print(f"Result: {result}")
    log_history(f"√{num} = {result}")


def modulus():
    num1 = get_float("Enter first number: ")
    num2 = get_float("Enter second number: ")

    if num2 == 0:
        print("Error: Cannot use modulus with zero.")
        log_history(f"{num1} % {num2} = Error (mod by zero)")
        return

    result = num1 % num2
    print(f"Result: {result}")
    log_history(f"{num1} % {num2} = {result}")


def average_numbers():
    count = get_int("How many numbers do you want to average? ")
    if count <= 0:
        print("Number must be greater than 0.")
        return

    numbers = []
    for i in range(count):
        num = get_float(f"Enter number {i + 1}: ")
        numbers.append(num)

    result = sum(numbers) / len(numbers)
    expression = ", ".join(str(n) for n in numbers)
    print(f"Result: {result}")
    log_history(f"average({expression}) = {result}")


def factorial_number():
    num = get_int("Enter a non-negative integer: ")
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        log_history(f"{num}! = Error (negative number)")
        return

    result = math.factorial(num)
    print(f"Result: {result}")
    log_history(f"{num}! = {result}")


def sum_unlimited_numbers():
    print("Enter numbers separated by space.")
    print("Example: 10 5 7 3")

    text = input("Numbers: ").strip()

    try:
        numbers = [float(x) for x in text.split()]
        if not numbers:
            print("You did not enter any numbers.")
            return

        result = sum(numbers)
        expression = " + ".join(str(n) for n in numbers)
        print(f"Result: {result}")
        log_history(f"{expression} = {result}")

    except ValueError:
        print("Invalid input. Only numbers separated by spaces are allowed.")


def show_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

        if not content:
            print("History is empty.")
        else:
            print("\n" + "=" * 40)
            print("HISTORY")
            print("=" * 40)
            print(content)

    except FileNotFoundError:
        print("History file does not exist yet.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-12): ").strip()

        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            multiply_numbers()
        elif choice == "4":
            divide_numbers()
        elif choice == "5":
            power_numbers()
        elif choice == "6":
            square_root()
        elif choice == "7":
            modulus()
        elif choice == "8":
            average_numbers()
        elif choice == "9":
            factorial_number()
        elif choice == "10":
            sum_unlimited_numbers()
        elif choice == "11":
            show_history()
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 12.")


if __name__ == "__main__":
    main()