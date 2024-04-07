while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for Multiplication")
    print("Enter '/' for Division ")
    print("Enter 'q' to quit ")

    choice = input("Enter Choice:")

    if choice =='q':
        break
    if choice in ('+','-','*','/'):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == '+':
            print("Result:",num1 + num2)
        elif choice =='-':
            print("Result:",num1 - num2) 
        elif choice =='*':
            print("Result:",num1 * num2)
        elif choice =='/':
            if num2 !=0:
                print("Result:",num1/num2)
            else:
                print("Error!Divsion by Zero")
    else:
        print("Invalid input")