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