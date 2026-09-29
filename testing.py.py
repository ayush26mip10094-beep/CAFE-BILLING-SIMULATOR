import unittest
import tkinter as tk
from cafe_billing_app import CafeBillingSimulator

class TestCafeBillingSimulator(unittest.TestCase):
    def setUp(self):
        """Initialize Tkinter root and application instance before each test."""
        self.root = tk.Tk()
        self.app = CafeBillingSimulator(self.root)

    def tearDown(self):
        """Destroy the Tkinter root after each test."""
        self.root.destroy()

    def test_initial_totals(self):
        """Test subtotal and grand total on an empty receipt."""
        subtotal, discount_pct, discount_amount, tax, grand_total, order_details = self.app.calculate_totals()
        self.assertEqual(subtotal, 0.0)
        self.assertEqual(grand_total, 0.0)
        self.assertEqual(len(order_details), 0)

    def test_single_item_calculation(self):
        """Test calculation when ordering 1 Espresso (120 INR + 5% GST)."""
        self.app.qty_vars["Espresso"].set(1)
        subtotal, discount_pct, discount_amount, tax, grand_total, order_details = self.app.calculate_totals()

        self.assertEqual(subtotal, 120.0)
        self.assertEqual(tax, 6.0)  # 5% of 120
        self.assertEqual(grand_total, 126.0)

    def test_discount_applied(self):
        """Test 10% discount on 200 INR Cold Brew."""
        self.app.qty_vars["Cold Brew"].set(1)
        self.app.discount_var.set("10")
        
        subtotal, discount_pct, discount_amount, tax, grand_total, order_details = self.app.calculate_totals()

        self.assertEqual(subtotal, 200.0)
        self.assertEqual(discount_amount, 20.0)  # 10% of 200
        self.assertEqual(tax, 9.0)  # 5% of 180 (200 - 20)
        self.assertEqual(grand_total, 189.0)

    def test_reset_order(self):
        """Test reset functionality clears input variables."""
        self.app.qty_vars["Espresso"].set(2)
        self.app.discount_var.set("15")
        self.app.reset_order()

        self.assertEqual(self.app.qty_vars["Espresso"].get(), 0)
        self.assertEqual(self.app.discount_var.get(), "0")

if __name__ == "__main__":
    unittest.main()