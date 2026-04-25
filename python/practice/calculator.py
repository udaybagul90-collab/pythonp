select = "y"

while select != "n":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    choice = int(input ("""\nif you want to add the numbers, press 1
if you want to subtract the numbers, press 2
if you want to multiply the numbers, press 3
if you want to divide the numbers, press 4 \n"""))

    match choice:
        case 1: print("The sum is:", a + b)
        case 2: print("The subtraction is:", a - b)
        case 3: print("The multiplication is:", a * b)
        case 4: print("The division is:", a / b)

    select = input ("Do you want to continue? (y/n): ")
