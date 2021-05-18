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

# print 12 with 10 leading spaces
str = "12"
print(str + 10 * ' ')
print(str.rjust(10))
print(str.ljust(10))




