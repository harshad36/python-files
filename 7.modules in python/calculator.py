'''
Calculator:Console based Application
=========
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit

Enter your Choice:2

'''
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")
    print("5. Exit")

    print()

    ch=int(input("Enter choice:"))

    if ch==1:
        x=int(input("Enter first number:"))
        y=int(input("enter second number:"))
        z=x+y
        print("addition is:",z)

    elif ch==2:
        x=int(input("Enter first number:"))
        y=int(input("enter second number:"))
        z=x-y
        print("division is:",z)

    elif ch==3:
        x=int(input("Enter first number:"))
        y=int(input("enter second number:"))
        z=x*y
        print("multiplication is:",z)

    elif ch==4:
        x=int(input("Enter first number:"))
        y=int(input("enter second number:"))
        z=x/y
        print("division is:",z)
    elif ch==5:
        print("Exit from program. Thank you for using service!!!!!")
        break
    else:
        print("Please enter valid choice between 1 to 5!!!!!")

