import tkinter as tk
from tkinter import messagebox

def calulate_interest():
    """Get inputs, compute interests, and show the results."""
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        simple_interest = (principal * time * rate) / 100

        amount = principal * ((1 + rate / 100) ** time)
        compound_interest = amount - principal

        label_si_result.config(text=f"Simple interest: {simple_interest:.2f}")
        label_ci_result.config(text=f"Compound interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")  

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")
root.resizable(False, False)

label_principal = tk.Label(root, text= "Principal Amount ($):")
label_principal.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=1, pady=10)

label_time = tk.Label(root, text="Time period (years):")
label_time.grid(row=1, column=1, padx=10,pady=10, sticky="e")

entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=10)

label_rate = tk.Entry(root)
label_rate.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=10, pady=10)

btn_calculate = tk.Button(root, text="Calculate Interest", command=calulate_interest)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=20)

label_si_result = tk.Label(root, text="Simple Interest: ")
label_si_result.grid(row=4, column=0, columnspan=2, pady=5)

label_ci_result = tk.Label(root, text="Compound Interest: ")
label_ci_result.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()