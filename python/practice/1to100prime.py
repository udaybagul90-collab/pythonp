sum = 0 
for j in range(3,101):
     
    number = j
    flag =0
    for i in range(2,number):
        if number % i == 0 :
            flag = 1
            break
    if flag == 0:
        print(f"{number} is a prime number")
        sum = number + sum
        
        
    else:
        pass

print(f"The sum of prime numbers from 1 to 100 is {sum}")

    