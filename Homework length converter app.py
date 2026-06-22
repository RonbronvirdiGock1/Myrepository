import tkinter as tk 
def convert_inches_to_cm():
    """
    This function gets the length in inches from the input field,
    converts it to centimeters, and displays the result.
    """
    try:

        inches_str = entry_inches.get()

        inches = float(inches_str)

        centimeters = inches * 2.54

        result_label.config(text=f"{inches} inches is {centimeters:.2f} cm") # '.2f' means show 2 decimal places

    except ValueError:

        result_label.config(text="Please enter a valid number for inches!")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x200")

label_inches = tk.Label(root, text="Enter length in inches:")
label_inches.pack(pady=10) 

entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

convert_button = tk.Button(root, text="Convert to Centimeters", command=convert_inches_to_cm)
convert_button.pack(pady=10)
result_label = tk.Label(root, text="Result will show here.")
result_label.pack(pady=5)

root.mainloop()