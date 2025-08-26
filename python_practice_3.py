# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# We can use the for statement to iterate through a sequence
# fhand (file handler)

xfile = open('mbox.txt')
for cheese in xfile: # iterates through each line in the file
    print(cheese)
    
# Counting lines in a file

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print("Line Count: ", count)

# Searching through a file

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Removes whitespace from the right-hand side
    if line.startswith('From:'):
        print(line)
    else:
        continue # Skips a line
    
    
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Removes whitespace from the right-hand side
    if not 'gordon' in line:
        continue
    print(line)
        
# Can prompt user input

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)