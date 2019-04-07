while True:
    print("options:")
    print("'add' adds two numbers")
    print("'subtract' subtracts two numbers")
    print("'multiply' multiplies 2 numbers")
    print("'divide' divides two numbers")
    print("quit")
    user_input = input(": ")

    if user_input == "quit":
        break
    
    elif user_input == "add":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a second number: "))
        result = str(num1+num2)
        print(">>>"+result)
    elif user_input == "subtract":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a second number: "))
        result = str(num1-num2)
        print(">>>"+result)
    elif user_input == "multiply":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a second number: "))
        result = str(num1*num2)
        print(">>>"+result)
    elif user_input == "divide":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a second number: "))
        result = str(num1/num2)
        print(">>>"+result)
    else:
        print("unknown input")
