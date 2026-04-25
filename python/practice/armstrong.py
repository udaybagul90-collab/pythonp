num = 153
temp = num
sum = 0

while num != 0:
    rem = num % 10
    sum += (pow(rem,3))
    num = num//10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")