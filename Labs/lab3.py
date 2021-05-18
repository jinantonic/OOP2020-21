# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
             sys.exit("We would have needed a word not a number")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        # concatenation is used here and we have to create the new_word because we can't just do the assignment of the value of these different positions
        # swap 3rd and 2nd around and add the rest of the word

        if len(self.user_input) > 3:
            new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] \
                       + self.user_input[3:]
             # from the 4th position to the end
             # backslash means i just broke the line here. Just way of breaking the line and this doesn't change the code
        elif len(self.user_input) <= 3:
            new_word = self.user_input
        else:  # here we assume this word is just one character long or the space character
            print("try again")
            new_word = False

        print(new_word)


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

        # one solution for full sentence
        # 문자열의 끝에 .strip()을 붙이면 문자열의 맨앞, 맨뒤  whitespace가 제거됨. 담, 중간중간의 whitespace는 제거되지 않음
        # split 함수는 문자열을 나뉘어서 나뉜 문자열의 리스트를 반환.
        # split 함수에 아무 인자도 없으면 공백을 기준으로 문자열을 분리한 문자열들의 리스트 반환
        # split 함수에 주는 인자는 분리문자로, 인자를 주면 문자열을 그 문자를 기준으로 분리
        sentence = self.user_input.strip().split()


        # get the word from the sentence
        # enumerate 함수는 for문과 함께 자주 사용. enumerate는 열거하다 라는 단어
        # 파이썬에서는 list, tuple, string 등 여러가지 자료형을 입력받으면 인덱스 값을 포함하는 enumerate 객체를 돌려
        # We used enumerate here because we actually need to know where we are
        for index, word in enumerate(sentence):
            # check the length of the word > 3
            if len(word) > 3:
                # swap the indice of 2 and last element
                temp_word = list(word) # We use a list for item assignment, but could also just use another new string variable
                # Or i take one before that because when we do find a punctuation, we need to preserve the location in it
                # If you don't check for it when you have commas or dots in it, it will actually swap it around as well
                # We preserve the punctuation element here
                if(',' in temp_word) or ('.' in temp_word):
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3] # 음수 인덱스 -3 -> 뒤에서 세번째 요소
                    temp_word[-3] = temp
                else:
                    # split the word in to a list of characters and swap
                    # this swap leaves first and last in tact
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                # join the characters together and form the word
                # This is the line why i needed my enumeration form.
                # join 함수는 리스트의 문자열들을 합치는 역할을 함. 이 밑 방법은 단순히 문자열을 붙히기만 함
                # 이어줄 문자 사이에 특정 문자를 넣고싶다면 "특정문자열".join(리스트)
                swapped_word = ''.join(temp_word)
                # replace the previous word at that position with the new swapped word
                sentence[index] = swapped_word
            else:
                # since the length of the word <3, don't swap the word
                sentence[index] = word

        # join all the words with a space
        the_swap = ' '.join(sentence)
        # print word
        print(the_swap)

word_scrambler = WordScramble()
word_scrambler.scramble()
