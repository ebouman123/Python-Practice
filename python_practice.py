smallest = None
print("Before:", smallest)
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i
    print("Loop:", i, smallest)
print("Smallest:", smallest)

