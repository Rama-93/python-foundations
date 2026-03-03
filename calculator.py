while True:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    op = (input("Choose the operator(+,-,*,/):\n"))
    if op == "+":
        print("result:", first_num+second_num)
    elif op == "-":
        print("result:", first_num-second_num)
    elif op == "*":
        print("result:", first_num*second_num)
    elif op == "/":
        if second_num == 0:
            print("Cannot be divided by zero")
        else:
            print("result:", first_num/second_num)
    else:
        print("Invalid operator")
    choice = input("Do you want to continue?(Yes/No):")
    if choice.lower()!= "yes":
       print("Exiting calculator.")
       break