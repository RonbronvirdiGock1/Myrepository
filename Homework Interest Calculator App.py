import tkinter as tk
import math 
def calculate_interest():
    """
    This function gets the principal, time, and rate from the input fields,
    calculates simple and compound interest, and displays the results.
    """
    try:

        principal_str = entry_principal.get()
        time_str = entry_time.get()
        rate_str = entry_rate.get()

        principal = float(principal_str)
        time = float(time_str)
        rate = float(rate_str)

        simple_interest = (principal * time * rate) / 100

        amount_compound = principal * math.pow((1 + rate / 100), time)
        compound_interest = amount_compound - principal

        si_result_label.config(text=f"Simple Interest: ₹{simple_interest:.2f}")
        ci_result_label.config(text=f"Compound Interest: ₹{compound_interest:.2f}")

    except ValueError:

        si_result_label.config(text="Simple Interest: Please enter valid numbers.")
        ci_result_label.config(text="Compound Interest: Please enter valid numbers.")
    except Exception as e:

        si_result_label.config(text=f"An error occurred: {e}")
        ci_result_label.config(text="") 

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x350") 
root.config(bg="#F0F8FF") 

label_principal = tk.Label(root, text="Principal Amount (₹):", font=("Arial", 12), bg="#F0F8FF")
label_principal.pack(pady=5)
entry_principal = tk.Entry(root, width=30, font=("Arial", 12))
entry_principal.pack(pady=2)

label_time = tk.Label(root, text="Time Period (Years):", font=("Arial", 12), bg="#F0F8FF")
label_time.pack(pady=5)
entry_time = tk.Entry(root, width=30, font=("Arial", 12))
entry_time.pack(pady=2)

label_rate = tk.Label(root, text="Rate of Interest (% per annum):", font=("Arial", 12), bg="#F0F8FF")
label_rate.pack(pady=5)
entry_rate = tk.Entry(root, width=30, font=("Arial", 12))
entry_rate.pack(pady=2)

calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest,
                             font=("Arial", 13, "bold"), bg="#90EE90", fg="darkgreen",
                             activebackground="#32CD32")
calculate_button.pack(pady=15)

si_result_label = tk.Label(root, text="Simple Interest: ", font=("Arial", 12), bg="#F0F8FF", fg="blue")
si_result_label.pack(pady=5)

ci_result_label = tk.Label(root, text="Compound Interest: ", font=("Arial", 12), bg="#F0F8FF", fg="red")
ci_result_label.pack(pady=5)

root.mainloop()