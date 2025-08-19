name = "Gordon"
age = 9
occupation = "House Cat"

print(name + " is a " + occupation + " and he is", age, "years old.")

def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
# You can implement it with a ternary operator instead

def is_adult_ternary(age):
    return True if age > 18 else False
    
is_adult(age)

# You can append to a string using +=
name += " Bouman"
print(name)

# You can convert a number to a string using the str class constructor
str(8)

# A string can be multiple lines if you use triple quotes
print('''Gordon is
      a little kitty''')
