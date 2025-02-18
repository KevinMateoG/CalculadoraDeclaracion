import unittest
import main

class rent_text(unittest.TestCase):
    def normal_text(self):
        
        uvt_value = 47_065
        gross_income = 100_000
        costs_deductions = 10_000_000
        exempt_income = 5_000_000
        tax_discounts = 500_000
        withholdings = 1_000_000
        patrimony = 200_000_000
        rate = 28
        
        rate = rate/100

        expected_exit = 22_300_000

        actual_exit = main.calculated_tax()




if __name__ == '__main__':
    unittest.main()
