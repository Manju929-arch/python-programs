# Original string
text = "hello World 123"

# capitalize() → Converts first character to uppercase
print(text.capitalize())

# casefold() → Converts string to lowercase (stronger than lower)
print(text.casefold())

# count(str) → Returns number of occurrences of substring
print(text.count("o"))

# encode(encoding) → Encodes string to bytes
print(text.encode("utf-8"))

# endswith(str) → Checks if string ends with given suffix
print(text.endswith("123"))

# find(str) → Returns index of first occurrence, -1 if not found
print(text.find("World"))

# index(str) → Like find() but raises error if not found
print(text.index("World"))

# isalnum() → Checks if string contains only alphabets and numbers
print(text.strip().isalnum())

# isalpha() → Checks if string contains only alphabets
print(text.strip().isalpha())

# isascii() → Checks if all characters are ASCII
print(text.isascii())

# isdecimal() → Checks if string contains only decimal digits
print("123".isdecimal())

# isdigit() → Checks if string contains only digits
print("123".isdigit())

# isidentifier() → Checks if valid Python identifier
print("variable_name".isidentifier())

# islower() → Checks if all characters are lowercase
print("hello".islower())

# isnumeric() → Checks if string contains numeric characters
print("123".isnumeric())

# isspace() → Checks if string contains only whitespaces
print("   ".isspace())

# istitle() → Checks if string is in title case
print("Hello World".istitle())

# isupper() → Checks if all characters are uppercase
print("HELLO".isupper())

# lower() → Converts string to lowercase
print(text.lower())

# lstrip([chars]) → Removes leading characters
print(text.lstrip())

# replace(old, new) → Replaces substring
print(text.replace("World", "Python"))

# rfind(str) → Finds last occurrence
print(text.rfind("o"))

# rindex(str) → Like rfind() but raises error if not found
print(text.rindex("o"))

# rstrip([chars]) → Removes trailing characters
print(text.rstrip())

# startswith(str) → Checks if string starts with prefix
print(text.strip().startswith("hello"))

# swapcase() → Swaps uppercase to lowercase and vice versa
print(text.swapcase())

# title() → Converts string to title case
print(text.title())

# upper() → Converts string to uppercase
print(text.upper())