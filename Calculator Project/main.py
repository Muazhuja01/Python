import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result},"
                       f" or type 'n' to start a new calculation,"
                       f" or 'x' to close the calculator: \n").lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            should_continue = False
            print("\n" * 20)
            calculator()
        elif choice == "x":
            print("Closing Calculator...")
            return
calculator()