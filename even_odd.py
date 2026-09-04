number = 5
if number % 2 == 0:
    print(f"{number} is an even number.")
else:  
    print(f"{number} is an odd number.")

# Now getting even odd number from user input
userNumber = int(input("Enter a number to ceck even or odd: "))
if userNumber % 2 == 0:
    print(f"{userNumber} is an even number.")
else:
    print(f"{userNumber} is an odd number.")