mark = int(input("Enter your mark: "))

if mark > 91 and mark <= 100:
    print("grade A")
elif mark > 71 and mark <=91:
    print("grade B")
elif mark > 51 and mark <= 71:
    print("grade C")
elif mark > 35 and mark <= 51:
    print("grade D")
elif mark > 0 & mark <= 35:
    print("grade F")
else:
    print("invalid mark")
