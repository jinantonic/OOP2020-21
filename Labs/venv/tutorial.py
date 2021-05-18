names = ["Bianca", "Bryan", "Susan"]

# names.insert(len(names), "paul")
print(names[:], end = " ") #list indicated by the bracket



for name in names:
    print(name) #Every element

for i in range(10):
    print(i, end="*")

print("\n")
my_numbers = [10, 20, 30, 40]
for i in range(len(my_numbers)):
    print(my_numbers[i], end="")

print("\n")
index = 0
while index < len(my_numbers):
    print(my_numbers[index])
    index += 1

fruits = ("apple", "banana", "pear")
    print(fruit)

for index, fruit in enumerate(fruits):
        print("Index is %d and formatting value is %s" % (index, fruit))


my_sum = 0
for i in range(1,11):
    my_sum += i
print("\nSum of first 10 natural numbers: ", my_sum)

for i in range(2, 26, 2):
    print(i, end=" ")

price = input("\nHow much does it cost ") #input always returns the string

if price.isdigit():
#if price == "1" : #You can use either "1" or 1
    print('yaay')
else:
    print('nay')


if float(price) >= 1.00:
    tax = 0.07
#   print(tax)
else:
    tax = 0
#print(tax) #after line 26, we are jumping right into 30 if we don't put the indentation
print("\nTax is: ", tax)
# print("tax" if float(price) >= 1.00 else "somethingelse")