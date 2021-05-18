# iterate over a file
fo = open('plaintext.txt', 'r')
print(fo.read())

fo = open('plaintext.txt', 'r')
for line in fo:
    print(line)

#fo = open('plaintext.txt', 'r')
#for line in fo:
#    line = line.splitlines()
#print(line)


# iterate over a list
list = ['cat', 'dog', 'lion', 'zerba', 'flamingo']
for i in list:
    print(i)

for index, number in enumerate(list):
    print(index, number)

# Format a string in a print() function to display 
# the number 12 with 10 leading space characters
str = "12"
print(str + 10 * ' ')
print(str.rjust(10))
print(str.ljust(10))

# True or false
print('123'.isdigit())
print('123abc'.isdigit())
print('abc'.isdigit())
print('1 2 3'.isdigit())
print('1 2 3'.isalpha())

# Listing 1(a)
my_input = input('tell me a letter between a and c >')

if my_input == 'a':
    print("a was input")
elif my_input == 'b':
    print("b was input")
elif my_input == 'c':
    print("c was input")
else:
    print("wrong letter, sorry.")

# Listing 1(b)
my_input = input('tell me a letter between a and c >')

if(my_input == 'a'):
    print("a was input")
if(my_input == 'b'):
    print("b was input")
if(my_input == 'c'):
    print("c was input")
else:
    print("wrong letter, sorry.")