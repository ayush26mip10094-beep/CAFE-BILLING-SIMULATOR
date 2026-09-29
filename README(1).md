# Cafe Billing Simulator

## About the Project

This is a simple **Cafe Billing Simulator** made as a college student project using Python.

I made this project to understand how a small billing system can be created with Python. The project has a graphical user interface (GUI), so the user does not need to type commands in the terminal.

The application is called **Mayuri Lounge - Billing System** and it creates a live receipt while items and quantities are selected.

## Technologies Used

- Python
- Tkinter
- `datetime` module

Tkinter is used to create the graphical interface, and `datetime` is used to show the current date and time on the receipt.

## Features

- Displays cafe menu items and their prices.
- Allows the user to select item quantities.
- Automatically calculates the subtotal.
- Allows a discount percentage to be entered.
- Calculates 5% GST.
- Shows the grand total.
- Updates the receipt automatically.
- Has a **Reset** button to clear the order.
- Has a **Print / Save** button that processes the bill.
- Shows a warning if no item is selected.
- Shows an order confirmation after payment processing.

## Menu Items

The program currently contains these items:

| Item | Price (₹) |
|---|---:|
| Espresso | 120 |
| Cappuccino | 160 |
| Iced Latte | 180 |
| Cold Brew | 200 |
| Croissant | 150 |
| Chocolate Muffin | 130 |
| Club Sandwich | 220 |
| Cheesecake | 250 |
| Hot Tea | 60 |
| Brownie with icecream | 180 |

## How the Billing Works

The program follows these basic steps:

1. Select the quantity of cafe items.
2. The program calculates the price of each selected item.
3. It adds all item prices to calculate the subtotal.
4. A discount can be entered as a percentage.
5. The discount is subtracted from the subtotal.
6. GST of 5% is calculated on the amount after discount.
7. The final amount is displayed as the **Grand Total**.
8. The user can process the bill using **Print / Save**.

### Formula Used

```text
Discount Amount = Subtotal × (Discount % / 100)

Taxable Amount = Subtotal - Discount Amount

GST = Taxable Amount × 5%

Grand Total = Taxable Amount + GST
```

## Requirements

You need:

- Python 3.x
- A computer with Tkinter support

Tkinter normally comes with standard Python installations on Windows.

## How to Run the Project

### Step 1: Install Python

Download and install Python 3 from the official Python website if it is not already installed.

### Step 2: Save the Python File

Keep the Python file and README file in the same project folder.

Example:

```text
Cafe Billing Project/
│
├── cafe billing simulator(1).py
└── README.md
```

### Step 3: Run the Program

Open Command Prompt or a terminal in the project folder and run:

```bash
python "cafe billing simulator(1).py"
```

If your computer uses `python3`, you can use:

```bash
python3 "cafe billing simulator(1).py"
```

## How to Use the Application

1. Open the program.
2. Choose quantities using the quantity boxes.
3. Enter a discount if required.
4. Check the live receipt on the right side.
5. Click **Print / Save** to process the bill.
6. After the bill is confirmed, the order is reset.
7. Click **Reset** anytime to clear the current order.

## Project Structure

The main class in the program is:

```text
CafeBillingSimulator
```

Important functions used in the program are:

- `__init__()` - starts the application and sets the basic window properties.
- `build_ui()` - creates the menu, buttons, receipt area, and other GUI elements.
- `calculate_totals()` - calculates subtotal, discount, GST, and grand total.
- `update_receipt()` - updates the receipt shown on the screen.
- `reset_order()` - clears the selected items and discount.
- `process_payment()` - confirms the bill and shows the payable amount.

## GST

The program uses a fixed GST rate of **5%**.

```python
self.tax_rate = 0.05
```

The GST is calculated after applying the discount.

## What I Learned From This Project

While making this project, I learned about:

- Python classes and objects.
- Tkinter GUI programming.
- Variables and dictionaries.
- Functions and methods.
- Loops and conditional statements.
- Exception handling using `try` and `except`.
- Taking user input through GUI widgets.
- Performing calculations using Python.
- Updating information dynamically in a GUI.
- Creating a simple billing workflow.

## Limitations

This is a basic student-level billing simulator. Some features that could be added in the future are:

- Saving bills to a file.
- Printing an actual physical receipt.
- Adding customer details.
- Adding different tax rates.
- Maintaining a sales history.
- Adding a database.
- Adding login functionality.
- Adding stock/inventory management.
- Adding a proper payment method selection.

## Future Improvements

In the future, I would like to make the project more complete by connecting it to a database and adding features such as customer records, bill history, inventory management, and actual receipt generation.

## Conclusion

This Cafe Billing Simulator is a simple Python GUI project that demonstrates how basic programming concepts can be combined to create a useful application. It is designed as a student project and can be improved further as I learn more Python and software development.

## Author

**Student Project**

Made using Python and Tkinter.
