import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.menu_item = {
            "FRIES MEAL" : 2,
            "LUNCH MEAL" : 2,
            "BURGER MEAL" : 3,
            "PIZZA MEAL" : 4,
            "CHEESE BURGER" : 2.5,
            "DRINKS" : 1
        }

        self.exchange_rate = 120

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, achor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restaunt Order Mangement",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_item.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font={"Arial", 12}
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantitiy_entry = ttk.Entry(frame, width=5)
            quantitiy_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantitiy_entry
        
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            front=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD","BDT")
        )
        currency_dropdown.grid(
            row=len(self.menu_item) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)

        self.currency_var.trace_add('write , self.update_menu_prices')

        order_botton = ttk.Button(
            frame,
            text="Plave Order",
            command=self.place_order
        )
        order_botton.grid(
            row=len(self.menu_item) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def upadate_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1

        for item, ladel in self.menu_labels.items():
            price = self.menu_item[item] *rate 
            label.config(text=f"{item} ({symbol}{price}:")

    def place_order(self):
        total_cost = 0
        oder_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "৳"  if currency == "BDT" else "$"

