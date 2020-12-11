# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

# Class to handle file management for file writing.
# Class Document receives the file name at initialisation.
class Document:
    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name

    def insert(self, character):
        if type(character) != str:
            raise ValueError("The inserted character has to be the string.")

        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        del self.characters[self.cursor]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        if type(steps) is not int:
            raise TypeError("The amount of steps the cursor should be forwarded to be an int.")

        try:
            if steps < len(self.characters):
                print("The cursor's movement has to be shorter than the whole length of the character")
        except:
            raise TypeError("Enter the movement of cursor in the range")

        self.cursor += steps

    def backward(self, steps):
        if type(steps) is not int:
            raise TypeError("The amount of steps to go back has to be an int.")

        try:
            if steps > len(self.characters):
                print("The cursor's movement has to be shorter than the whole length of the character")
        except:
            raise TypeError("Enter the movement of cursor in the range")

        self.cursor -= steps


# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'jina park is from korea'

for letter in characters:
    doc.insert(letter)

doc.backward(14)
doc.delete()
doc.insert('b')
doc.save()

