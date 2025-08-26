# the "in" keyword can be used to check to see if one string is in another string (returns boolean)

fruit = "banana"
print("n" in fruit) # True
print("m" in fruit) # False
print("nan" in fruit) # True

if "a" in fruit:
    print("Found it!") # "Found it!"
    
# String Library (methods)

greet = "Hello Gordon"
lowercaseGreet = greet.lower()
print(lowercaseGreet) # "hello gordon"
print(greet) # "Hello Gordon"

i = greet.find("lo")
print(i)

# open() can be used to read files

#fhand = open("stuff.txt")

# \n can be used to start a new line, these are at the end of every lines in text files

print("Hello\nWorld!")
# Hello
# World!

