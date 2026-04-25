# List of fruits
List1 = ['apple', 'banana', 'mango']

# String to search
search_item = input("Enter fruit to search: ")

# Flag to check if found
found = False

# Search using for loop
for fruit in List1:
    if fruit == search_item:
        found = True
        break

# Display result
if found:
    print(search_item, "is found in the list")
else:
    print(search_item, "is not found in the list")