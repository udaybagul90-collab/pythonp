list = ["appple","banana","graps","mango"]

for item in list:
    if item == "banana":
        continue
    print (item)

for item in list:
    if item == "graps":
        break
    print (item)