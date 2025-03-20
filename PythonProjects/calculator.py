    """
    * The user selects an option from the menu.
    * The program prompts for input based on the selected operation.
    * The result is calculated using the respective function.
    * Handles division by zero and negative square root cases gracefully.
    * The program repeats until the user chooses to exit.
    
    """
    
import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0: 
        return "Error! Division by zero"
    else: 
        return x / y
    
def pow(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Square root of negative numbers not allowed"
    else:
        return math.sqrt(x)

def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")
    
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("\nExiting.... Goodbye!")
            break
    
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {mul(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {div(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} ** {num2} = {pow(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter a number: "))
            print(f"Square root of {num} = {sqrt(num)}")
        
        else:
            print("Invalid input! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
