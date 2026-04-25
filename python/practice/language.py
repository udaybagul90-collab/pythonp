select = "y"
while select != "n":
    choice = int(input("Enter The Choice"))

    match choice:
        case 1: print("gujarati")
        case 2: print("hindi")
        case 3: print("english")
        case 4: print("french")
        case 5: print("spanish")
        case 6: print("german")
        case _ : print("Invalid Choice")
    select = input("Do you want to continue? (y/n): ")