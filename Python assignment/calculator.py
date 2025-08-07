# Simple Calculator Program

def calculator():
    print("\n Simple Python Calculator")
    print("(Type 'quit' to exit)\n")
    
    while True:
        try:
            num1 = input("Enter first number: ").strip()
            if num1.lower() in ['quit', 'exit']:
                break
            num1 = float(num1)
            
            num2 = input("Enter second number: ").strip()
            if num2.lower() in ['quit', 'exit']:
                break
            num2 = float(num2)
            
            operation = input("Enter operation (+, -, *, /): ").strip()
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2 if num2 != 0 else "Error: Can't divide by zero"
            else:
                print("Invalid operation! Please use +, -, *, or /\n")
                continue
                
            print(f"\n Result: {num1} {operation} {num2} = {result}\n")
            
        except ValueError:
            print("Please enter valid numbers!\n")
        except Exception as e:
            print(f"Something went wrong: {e}\n")
    
    input("\nPress Enter to exit...")
calculator()