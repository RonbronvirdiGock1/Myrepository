class StringReverser:
    def __init__(self, input_string):
        self.original_string = input_string

    def reverse_letter_by_letter(self):
        reversed_string = self.original_string[::-1]
        return reversed_string

my_sentence = "Codingal is fun"
reverser_object = StringReverser(my_sentence) 

reversed_letters = reverser_object.reverse_letter_by_letter()

print(reversed_letters)