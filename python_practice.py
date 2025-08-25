smallest = None
print("Before:", smallest)
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i
    print("Loop:", i, smallest)
print("Smallest:", smallest)

# is and is not are similar to, but stronger than ==

smallest = None
print("Before")
for value in [3, 41, 12, 9, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print("After", smallest)

# In Python, strings are treated like arrays in JS (indexed)

for letter in "Banana":
    print(letter)
    
# Slicing strings

s = "Monty Python"
# M o n t y   P y t h o  n
# 0 1 2 3 4 5 6 7 8 9 10 11
print(s[0:4])  # Prints "Mont"
print(s[6:7])  # Prints "P"
print(s[6:20]) # Prints "Python"
print(s[:2])   # Prints "Mo"
print(s[8:])   # Prints "thon"
print(s[:])    # Prints "Monty Python"


# String Concatenation

a = "Hello"