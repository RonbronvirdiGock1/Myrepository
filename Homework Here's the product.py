import tkinter
def calculate_product():
    """
    This function gets the numbers, calculates their product,
    and displays the result.
    """
    try:
        num1_str = entry1.get()
        num2_str = entry2.get()

        number1 = float(num1_str)
        number2 = float(num2_str)

        product = number1 * number2

        result_label.config(text=f"The product is: {product}")

    except ValueError:

        result_label.config(text="Please enter valid numbers!")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

root = tkinter.Tk()
root.title("Product Calculator")

label1 = tkinter.Label(root, text="Enter first number:")
label1.pack(pady=5)

entry1 = tkinter.Entry(root)
entry1.pack(pady=5)

label2 = tkinter.Label(root, text="Enter second number:")
label2.pack(pady=5)

entry2 = tkinter.Entry(root)
entry2.pack(pady=5)

calculate_button = tkinter.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=10)

result_label = tkinter.Label(root, text="The product will appear here.")
result_label.pack(pady=5)

root.mainloop()