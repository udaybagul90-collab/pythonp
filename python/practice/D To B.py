num = 468
sum = 0
mul = 1

while num != 0:
    rem = num % 2
    num = num//2
    sum = (rem*mul) + sum
    mul *= 10
print(sum)
    

    