from tkinter import *

root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150")

label_inches = Label(root, text="Length in inches:")
label_inches.pack(pady=5)

entry_inches = Entry(root)
entry_inches.pack(pady=5)

result_label = Label(root, text="")
result_label.pack(pady=10)

def convert():
    """Read inches, convert to cm, and update the result label"""
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54

        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number!")    

convert_button = Button(root, text="Convert", command= convert)
convert_button.pack(pady=5)

root.mainloop()