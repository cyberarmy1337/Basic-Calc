def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

while True:
    
    print("Select the operation you want:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    user_input_00 = input(": ")

    if user_input_00 == "5":
        break
    elif user_input_00 in ("1", "2", "3", "4"):
        no1 = float(input("Enter the first number: "))
        no2 = float(input("Enter the second number: "))
        if user_input_00 == "1":
            print("Result is:", add(no1, no2))
        elif user_input_00 == "2":
            print("Result is:", subtract(no1, no2))
        elif user_input_00 == "3":
            print("Result is:", multiply(no1, no2))
        elif user_input_00 == "4":
            result = divide(no1, no2)
            if result == "Error: Cannot divide by zero":
                print(result)
            else:
                print("Result is:", result)
    else:
        print("Invalid input. Please enter a valid option.")



