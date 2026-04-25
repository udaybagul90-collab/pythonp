num = 10011011
p = 0
sum = 0

while num != 0:
    rem = num%10
    sum += (rem*pow(2,p))
    num = num//10
    p += 1
print(sum)