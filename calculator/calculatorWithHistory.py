HISTORY_FILE = "history.txt"


def show_history():
    file = open(HISTORY_FILE, "r")

    lines = file.readlines()

    if len(lines) == 0:
        print("No history found.")
    else:
        print("\n--- Calculation History ---")
        for line in reversed(lines):
            print(line.strip())

    file.close()


def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")


def save_to_history(expression, result):
    file = open(HISTORY_FILE, "a")
    file.write(expression + " = " + str(result) + "\n")
    file.close()


def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number (e.g., 5 + 3)")
        return

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return

    else:
        print("Invalid operator. Please use one of the following: +, -, *, /")
        return

    # Convert 5.0 to 5
    if result == int(result):
        result = int(result)

    print("Result:", result)

    save_to_history(user_input, result)


def main():
    print("------ Simple Calculator with History ------")

    while True:
        user_input = input(
            "\nEnter calculation (or type 'history', 'clear', 'exit'): "
        ).strip()

        if user_input.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        elif user_input.lower() == "history":
            show_history()

        elif user_input.lower() == "clear":
            clear_history()

        else:
            calculate(user_input)


main()