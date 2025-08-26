# Lists are like arrays in JS
# They can have any type of element (str, bool, int, object, list)
# Lists can be empty
# Just like JS, common to iterate through lists with for loops

# Concatenating Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# > [1, 2, 3, 4, 5, 6]
print (a)
# > [1, 2, 3]

# Slicing lists works the same as with strings
t = [1, 2, 3, 4, 5, 6, 7]
print(t[1:3])
# > [2, 3]
print(t[:4])
# > [1, 2, 3, 4]
print(t[3:])
# > [4, 5, 6, 7]

# There are the usual methods for lists (append, count, extend, index, insert, pop, remove, reverse, sort)

# Creating a list

cats = list()
cats.append("Gordon")
cats.append("Sammi")
print(cats)
# > ["Gordon", "Sammi"]

"Gordon" in cats
# > True

# sort() obviously sorts the list, and it changes the original list to be in that order
# max() min() gets the max/min int, len() gets the length of the list, sum() will sum the ints


# Strings and Lists

abc = 'With three words'
stuff = abc.split() # Finds spaces and splits the string into a list (treats multiple spaces as 1 space)
print(stuff)
# > ['With', 'three', 'words']

for word in stuff:
    print(word)
# > With
# > three
# > words

semicolon = 'the;fluffy;cat'
x = semicolon.split(";") # You can split by characters other than a space
print(x)
# > ['the', 'fluffy', 'cat']


# Example: Getting the date from an email line
# From: gordon.bouman@gmail.com Sat Jan 5 09:14:15 2025

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: ') : continue
    words = line.split()
    print(words[2])
    # > 'Sat'
    
# Can chain splits
line = 'From: gordon.bouman@gmail.com Sat Jan 5 09:14:15 2025'
words = line.split() # ['From:', 'gordon.bouman@gmail.com', 'Sat', 'Jan', 5, 09:14:15, 2025]
email = words[1] # ['gordon.bouman@gmail.com']
end = email.split('@') # ['gmail.com']

