# original string
text = "  hello python world  "

print("Original String:", text)

# remove extra spaces
print("Strip:", text.strip())

# convert to uppercase
print("Uppercase:", text.upper())

# convert to lowercase
print("Lowercase:", text.lower())

# replace word
print("Replace:", text.replace("python", "Java"))

# split into list
print("Split:", text.split())

# check startswith
print("Starts with 'hello':", text.strip().startswith("hello"))

# check endswith
print("Ends with 'world':", text.strip().endswith("world"))

# length of string
print("Length:", len(text))

# capitalize first letter
print("Capitalize:", text.strip().capitalize())