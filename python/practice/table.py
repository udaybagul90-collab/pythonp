choice = "y"
while choice != "n":
    num = int(input("Enter a number: "))

    for i in range(1,11):
        print(f"{i} X {num} = {i*num}")
    choice = input("Do you want to continue? (y/n): ")