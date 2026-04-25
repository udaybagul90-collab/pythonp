# Compare two numbers using if-else

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
    print(num2, "is less than", num1)
else:
    print(num2, "is greater than", num1)
    print(num1, "is less than", num2)
