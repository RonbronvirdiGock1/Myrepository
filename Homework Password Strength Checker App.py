import tkinter as tk
import random
import string 

WEAK_COLOR = "#FFCCCC"    
MEDIUM_COLOR = "#FFDDAA"  
STRONG_COLOR = "#CCFFCC"  
DEFAULT_COLOR = "lightgray" 
TEXT_COLOR = "black"     

def check_password_strength():
    """
    Checks the strength of the password based on its length
    and updates the strength_label with color feedback.
    """
    password = password_entry.get()
    length = len(password)

    if length < 6:
        strength_label.config(text="Strength: Weak", bg=WEAK_COLOR, fg=TEXT_COLOR)
    elif 6 <= length <= 10:
        strength_label.config(text="Strength: Medium", bg=MEDIUM_COLOR, fg=TEXT_COLOR)
    else: # length > 10
        strength_label.config(text="Strength: Strong", bg=STRONG_COLOR, fg=TEXT_COLOR)

def suggest_password():
    """
    Generates a strong, random password and displays it.
    """
    characters = string.ascii_letters + string.digits + string.punctuation

    password_length = random.randint(12, 16) 

    suggested = ''.join(random.choice(characters) for i in range(password_length))

    suggested_password_label.config(text=f"Suggested: {suggested}")

    password_entry.delete(0, tk.END) 
    password_entry.insert(0, suggested) 

    check_password_strength()

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.config(bg="lightblue") 

instruction_label = tk.Label(root, text="Enter your password:",
                             font=("Arial", 14), bg="lightblue", fg="darkblue")
instruction_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)

password_entry.bind("<KeyRelease>", lambda event: check_password_strength())

strength_label = tk.Label(root, text="Strength: ---",
                          font=("Arial", 12, "bold"), bg=DEFAULT_COLOR, fg=TEXT_COLOR,
                          relief="groove", bd=2, width=30, height=2)
strength_label.pack(pady=10)

check_button = tk.Button(root, text="Check Strength Now", command=check_password_strength,
                         font=("Arial", 12), bg="lightgreen", fg="darkgreen")
check_button.pack(pady=5)

separator = tk.Frame(root, height=2, bd=1, relief="sunken", bg="gray")
separator.pack(fill="x", padx=20, pady=10)

suggest_button = tk.Button(root, text="Suggest Password", command=suggest_password,
                           font=("Arial", 12), bg="gold", fg="darkred")
suggest_button.pack(pady=5)

suggested_password_label = tk.Label(root, text="Suggested: (Click button)",
                                    font=("Courier New", 10), bg="white", fg="black",
                                    relief="sunken", bd=1, width=40, height=2)
suggested_password_label.pack(pady=10)

root.mainloop()