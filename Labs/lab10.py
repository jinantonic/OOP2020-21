from abc import ABC, abstractmethod

class MathsGame(ABC):
    @abstractmethod
    def __init__(self):
        print("Welcome to the Math Game")

    @property
    @abstractmethod
    def user_input_property(self):
        pass

    @abstractmethod
    def play_game(self):
        pass

class FibonacciGame(MathsGame):
    def __init__(self):
        super().__init__()
        self.__input = 0

    @property
    def user_input_property(self):
        return self.__input

    @user_input_property.setter
    def user_input_property(self, value):
        self.__input = value

    def play_game(self):
        right_guesses = 0
        keep_playing = True

        while keep_playing:
            try:
                self.user_input_property = int(input("Enter 1 to play, Enter 2 to exit: "))
                if self.user_input_property not in range(1, 3):
                    print("Wrong input. Allowed are 1 to play or 2 to exit.")
            except:
                print("Enter a whole number: either 1 or 2")
                continue

            if self.user_input_property == 1:
                try:
                    terms = int(input("How many terms: "))

                    if terms != 0:
                        fibs = self.calculate_fibonacci(terms + 1)

                        print(fibs[:-1])

                        right_or_wrong = int(input("Guess the next number: "))

                        if right_or_wrong == fibs[-1]:
                            print("Well done")
                            right_guesses += 1
                        else:
                            print("Sorry, this was wrong.\n The right number is : ", fibs[-1])

                    else:
                        print("Nothing to play.")

                except:
                    print("Terms must be a whole number.")

            elif self.user_input_property == 2:
                print(f"You got {right_guesses} right this game!")

                keep_playing = False

    @staticmethod
    def calculate_fibonacci(terms):
        if type(terms) is not int:
            raise TypeError("Fibonacci terms need to be a whole number greater than zero.")

        fib_numbers = [] # lists that holds the fibonacci numbers

        if terms > 1:
            fib_numbers.extend([0, 1])

            before_before = 0
            before = 1

            for number in range(2, terms):
                # actual calculation
                current = before_before + before
                fib_numbers.append(current)

                # now fix variables for next run
                before_before = before
                before = current

        elif terms == 1:
            fib_numbers.append(0)

        elif terms <= 0:
            raise ValueError("Cannot do Fibonacci for 0 terms")

        return fib_numbers

# object instantiaiton
f = FibonacciGame()
f.play_game()

# display fibonacci terms using the static method
try:
    print(FibonacciGame.calculate_fibonacci(10))
except Exception as e:
    print(e)

