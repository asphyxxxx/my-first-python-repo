def calculator():
    print("===== Basic Calculator =====")
    
    operations = {
        '1': ('Add', lambda x, y: x + y),
        '2': ('Subtract', lambda x, y: x - y),
        '3': ('Multiply', lambda x, y: x * y),
        '4': ('Divide', lambda x, y: x / y if y != 0 else 'Error: Division by zero')
    }
    
    while True:
        print("\nAvailable operations:")
        for key, (operation, _) in operations.items():
            print(f"{key}. {operation}")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thanks for using the calculator!")
            break
            
        if choice not in operations:
            print("Invalid choice! Please try again.")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            operation_name, operation = operations[choice]
            result = operation(num1, num2)
            
            print(f"\nResult: {num1} {operation_name.lower()} {num2} = {result}")
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculator()
