# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: Lab wk8 - Word Games

# base class
class WordGames:
    def __init__(self):
        self.__my_words = input("Please enter a word or sentence: ")
        if self.__my_words.isdigit():
            sys.exit("We would have needed a word not a number")

    @property
    def the_words(self):
        return self.__my_words

    def word_play(self):
        print("User input was: " + self.the_words)

class WordDuplication(WordGames): # you implement this and provide docstrings
    def word_play(self):
        print("User input doubled: ")
        print(self.the_words + '' + self.the_words)

class WordScramble(WordGames): # you implement this and provide docstrings
    def word_play(self):
        scrambled = ''
        list_of_words = self.the_words.split()
        tuple_of_punctuation = (',', '.', ';', '?', ' ', '!')

        for word in list_of_words:
            if (len(word) > 4 and word not in tuple_of_punctuation):
                scrambled += word[0] + word[-1] + word[2:-1] + word[1] + ' '
            else:
                print("Too few letters for scrambling: ", word)

        print(scrambled)


# prints the docstrings info
# if this class was a python module
#print(WordGames.__doc__)

# Create an instances of the classes here:
wg = WordGames()
wg.word_play()

wd = WordDuplication()
wd.word_play()

#print(WordScramble.__doc__)
ws = WordScramble()
ws.word_play()

