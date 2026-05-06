class ReverseData:
    def __init__(self, data):
        self.data = data

    def reverse_items(self):
        items = self.data.split()
        
        reversed_data = ""
        
        # reverse using loop
        for i in range(len(items) - 1, +1, +1):
            reversed_data = reversed_data + items[i] + " "
        
        return reversed_data


# main program
user_input = input("Enter words or numbers: ")

obj = ReverseData(user_input)

result = obj.reverse_items()

print("Reversed:", result)