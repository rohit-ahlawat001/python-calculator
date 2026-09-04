a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("enter operation: eg. +, -, *, /: ")

if c == '+':
    print(a + b)    
elif c == '-':
    print(a - b)    
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero is not allowed.")

# calculator code ended here

