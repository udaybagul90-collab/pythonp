num = 111
temp = num
sum =0
while num != 0:
    rem = num % 10
    num = num//10
    sum = (sum * 10) + rem

if sum == temp :
    print("Pelindrome number")
else:
    print("Not a Pelindrome number")