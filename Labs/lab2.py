#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2 Solution

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: ", message)

        # print only first and last of the sentence
        print("First character: " + message[0])
        print("Last character : " + message[-1])

        # use slice notation
        print("Print from position 3 to end: " + message[3:])
        print("Print up to prosition 3: " + message[:3])
        print("Prints everthing via slice: " + message[:])

        # escaping a character
        print("He said \"that\'s fantastic\"!")

        # find all a's in the input word and count how many there are
        lower_message = message.lower()
        print("all lower characters: " +lower_message)

        # str() converts an integer or a float into a string
        print("The first occurence of a is at position: " + str(lower_message.find('a')))
        print("There are "+ str(lower_message.count('a'))+ " a's in the word.")
        print("Total character count is: " +str(len(lower_message)))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        print(lower_message.replace('a', '-'))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        # split() returns a list of words in a string
        my_list = list(message.split(" "))
        print(my_list)

        # append a new element to the list and print:
        my_list.append('Jina')  # adding a new element 'Jina'
        print(my_list)

        # remove from the list in 3 ways
        print(my_list.pop(0))  # my_list[0] will be deleted
        print(my_list)

        my_list.remove('Jina')
        print(my_list)

        del my_list[-1:-2]
        print(my_list)

        # check if the word cake is in your input list:
        print('cake' in my_list)

        # reverse the items in the list and print:
        my_list.reverse()
        print(my_list)

        # reverse the list with the slicing trick:
        print(my_list[::-1])

        # print the list 3 times by using multiplication:
        print(my_list * 3)


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()