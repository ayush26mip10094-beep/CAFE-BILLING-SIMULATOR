import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class CafeBillingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Billing Simulator")
        self.root.geometry("820x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#F4F4F9")

        # Menu Items & Prices
        self.menu_data = {
            "Espresso": 120,
            "Cappuccino": 160,
            "Iced Latte": 180,
            "Cold Brew": 200,
            "Croissant": 150,
            "Chocolate Muffin": 130,
            "Club Sandwich": 220,
            "Cheesecake": 250,
            "Hot Tea": 60,
            "Brownie with icecream": 180
        }

        self.order_dict = {}
        self.tax_rate = 0.05  # 5% GST
        
        self.build_ui()

    def build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#3D2C2E", height=60)
        header.pack(fill=tk.X)
        title_label = tk.Label(
            header, text="☕ MAYURI LOUNGE - BILLING SYSTEM", 
            font=("Helvetica", 18, "bold"), fg="#FFFFFF", bg="#3D2C2E"
        )
        title_label.pack(pady=15)

        # Main Layout Frame
        main_frame = tk.Frame(self.root, bg="#F4F4F9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Menu Selection
        left_frame = tk.LabelFrame(
            main_frame, text=" Menu Items ", font=("Helvetica", 11, "bold"),
            bg="#FFFFFF", fg="#333333", padx=10, pady=10
        )
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Right Frame: Receipt & Actions
        right_frame = tk.LabelFrame(
            main_frame, text=" Live Receipt ", font=("Helvetica", 11, "bold"),
            bg="#FFFFFF", fg="#333333", padx=10, pady=10
        )
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Populate Menu
        row = 0
        self.qty_vars = {}
        
        # Headers
        tk.Label(left_frame, text="Item Name", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=5)
        tk.Label(left_frame, text="Price (₹)", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=0, column=1, sticky="e", pady=5)
        tk.Label(left_frame, text="Qty", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=0, column=2, padx=10, pady=5)

        row += 1
        for item, price in self.menu_data.items():
            tk.Label(left_frame, text=item, font=("Helvetica", 10), bg="#FFFFFF").grid(row=row, column=0, sticky="w", pady=4)
            tk.Label(left_frame, text=f"{price:.2f}", font=("Helvetica", 10), bg="#FFFFFF").grid(row=row, column=1, sticky="e", pady=4)

            qty_var = tk.IntVar(value=0)
            self.qty_vars[item] = qty_var

            spinbox = tk.Spinbox(
                left_frame, from_=0, to=20, width=4, textvariable=qty_var,
                font=("Helvetica", 10), command=self.update_receipt
            )
            spinbox.grid(row=row, column=2, padx=10, pady=4)
            spinbox.bind("<KeyRelease>", lambda e: self.update_receipt())
            row += 1

        # Discount & Payment Controls
        control_frame = tk.Frame(left_frame, bg="#FFFFFF")
        control_frame.grid(row=row, column=0, columnspan=3, sticky="we", pady=(20, 0))

        tk.Label(control_frame, text="Discount (%):", font=("Helvetica", 10), bg="#FFFFFF").grid(row=0, column=0, sticky="w")
        self.discount_var = tk.StringVar(value="0")
        discount_entry = tk.Entry(control_frame, textvariable=self.discount_var, width=5, font=("Helvetica", 10))
        discount_entry.grid(row=0, column=1, sticky="w", padx=5)
        discount_entry.bind("<KeyRelease>", lambda e: self.update_receipt())

        # Buttons
        btn_frame = tk.Frame(left_frame, bg="#FFFFFF")
        btn_frame.grid(row=row+1, column=0, columnspan=3, pady=15)

        tk.Button(
            btn_frame, text="Reset", command=self.reset_order, 
            bg="#D9534F", fg="white", font=("Helvetica", 10, "bold"), width=10, relief="flat"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame, text="Print / Save", command=self.process_payment, 
            bg="#5CB85C", fg="white", font=("Helvetica", 10, "bold"), width=12, relief="flat"
        ).pack(side=tk.LEFT, padx=5)

        # Receipt Display Area
        self.receipt_text = tk.Text(right_frame, width=38, height=22, font=("Courier", 9), bg="#FAFAFA", relief="solid", bd=1)
        self.receipt_text.pack(fill=tk.BOTH, expand=True)

        self.update_receipt()

    def calculate_totals(self):
        subtotal = 0.0
        order_details = []

        for item, price in self.menu_data.items():
            try:
                qty = self.qty_vars[item].get()
            except tk.TclError:
                qty = 0

            if qty > 0:
                item_total = price * qty
                subtotal += item_total
                order_details.append((item, qty, price, item_total))

        try:
            discount_pct = float(self.discount_var.get())
            if discount_pct < 0 or discount_pct > 100:
                discount_pct = 0.0
        except ValueError:
            discount_pct = 0.0

        discount_amount = subtotal * (discount_pct / 100)
        taxable_amount = subtotal - discount_amount
        tax = taxable_amount * self.tax_rate
        grand_total = taxable_amount + tax

        return subtotal, discount_pct, discount_amount, tax, grand_total, order_details

    def update_receipt(self):
        subtotal, discount_pct, discount_amount, tax, grand_total, order_details = self.calculate_totals()

        self.receipt_text.config(state=tk.NORMAL)
        self.receipt_text.delete(1.0, tk.END)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        receipt = f"{'BISTRO BY SAFAL':^36}\n"
        receipt += f"{'Special block VIT BHOPAL':^36}\n"
        receipt += f"Date: {now}\n"
        receipt += "-" * 36 + "\n"
        receipt += f"{'Item':<16} {'Qty':<4} {'Price':<6} {'Total':<6}\n"
        receipt += "-" * 36 + "\n"

        if not order_details:
            receipt += f"\n{'[ No Items Selected ]':^36}\n\n"
        else:
            for item, qty, price, total in order_details:
                name = item[:15]
                receipt += f"{name:<16} {qty:<4} {price:<6.0f} {total:<6.0f}\n"

        receipt += "-" * 36 + "\n"
        receipt += f"Subtotal: {'₹' + f'{subtotal:.2f}':>26}\n"
        if discount_amount > 0:
            receipt += f"Discount ({discount_pct:.0f}%): {'-₹' + f'{discount_amount:.2f}':>21}\n"
        receipt += f"GST (5%): {'₹' + f'{tax:.2f}':>27}\n"
        receipt += "=" * 36 + "\n"
        receipt += f"GRAND TOTAL: {'₹' + f'{grand_total:.2f}':>23}\n"
        receipt += "=" * 36 + "\n"
        receipt += f"{'Thank you for visiting!':^36}\n"

        self.receipt_text.insert(tk.END, receipt)
        self.receipt_text.config(state=tk.DISABLED)

    def reset_order(self):
        for item in self.qty_vars:
            self.qty_vars[item].set(0)
        self.discount_var.set("0")
        self.update_receipt()

    def process_payment(self):
        subtotal, _, _, _, grand_total, order_details = self.calculate_totals()
        if not order_details:
            messagebox.showwarning("Warning", "Please select at least one item to proceed.")
            return

        messagebox.showinfo(
            "Order Confirmed", 
            f"Bill Processed Successfully!\n\nTotal Amount Payable: ₹{grand_total:.2f}"
        )
        self.reset_order()

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeBillingSimulator(root)
    root.mainloop()