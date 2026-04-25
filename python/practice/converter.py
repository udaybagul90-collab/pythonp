choice = int(input("Enter your choice: \n1. Decimal to Binary\n2. Decimal to Octal\n3. Decimal to Hexadecimal"))

if choice == 1:
    slect = int(input("Enter Choice: \n1. decimal to binary\n2. binary to decimal\n"))
    if slect == 1:
        num = int(input("Enter a decimal number: "))
        sum = 0
        mul = 1
        
        while num != 0:
            rem = num %2
            num = num//2
            sum +=(rem*mul)
            mul *= 10
        print("Binary number: ",sum)
    elif slect == 2:
        print("Binary to Decimal")

#octal
if choice == 2:
    slect = int(input("Enter Choice: \n1. decimal to octal\n2. octal to decimal\n"))
    if slect == 1:
        num = int(input("Enter a decimal number: "))
        sum = 0
        mul = 1
        
        while num != 0:
            rem = num %8
            num = num//8
            sum +=(rem*mul)
            mul *= 10
        print("Octal number: ",sum)
    elif slect == 2:
        print("Octal to Decimal")
if choice == 3:
    slect = int(input("Enter Choice: \n1. decimal to hexadecimal\n2. hexadecimal to decimal\n"))
    if slect == 1:
        num = int(input("Enter a decimal number: "))
        sum = ""
        mul = 1
        list=  ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        
        while num != 0:
           rem = num%16
           num = num//16
           sum = list[rem]+sum
        print("Hexadecimal number: ",sum)
    elif slect == 2:
        print("Hexadecimal to Decimal")

        

