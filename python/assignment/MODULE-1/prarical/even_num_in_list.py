# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Empty list to store even numbers
even_numbers = []

# Loop to filter even numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Print result
print("Original list:", numbers)
print("Even numbers:", even_numbers)