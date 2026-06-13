import tkinter as tk
from datetime import date 

def calculate_age():
    """
    This function gets the birth date from the input fields,
    calculates the current age, and displays the result.
    """
    try:
     
        day_str = entry_day.get()
        month_str = entry_month.get()
        year_str = entry_year.get()

        birth_day = int(day_str)
        birth_month = int(month_str)
        birth_year = int(year_str)

        birth_date = date(birth_year, birth_month, birth_day)

        today = date.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your current age is: {age} years")

    except ValueError:

        result_label.config(text="Please enter valid numbers for Day, Month, and Year.")
    except Exception as e:

        result_label.config(text=f"An error occurred: {e}")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x300") 

label_day = tk.Label(root, text="Day:")
label_day.pack(pady=2)
entry_day = tk.Entry(root, width=5)
entry_day.pack(pady=2)

label_month = tk.Label(root, text="Month:")
label_month.pack(pady=2)
entry_month = tk.Entry(root, width=5)
entry_month.pack(pady=2)

label_year = tk.Label(root, text="Year:")
label_year.pack(pady=2)
entry_year = tk.Entry(root, width=7)
entry_year.pack(pady=2)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=15)

result_label = tk.Label(root, text="Your age will appear here.")
result_label.pack(pady=5)

root.mainloop()