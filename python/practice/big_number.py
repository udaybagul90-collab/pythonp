a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>b and a>c:
    print("The biggest number is:", a)
elif b>a and b>c:
    print("The biggest number is:", b)
elif c>a and c>b:
    print("The biggest number is:", c)