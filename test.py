import unittest
import main

class tests(unittest.TestCase):

    def test_normal_1(self):
        uvt_value = 47065
        gross_income = 100_000_000
        costs_deductions = 10_000_000
        exempt_income = 5_000_000
        tax_discounts = 500_000
        withholdings = 1_000_000
        patrimony = 200_000_000
        rate = 0.28
    
        resultado_esperado = 22_300_000

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony, rate)
        
        self.assertEqual(calculated_tax, resultado_esperado)

if __name__ == '__main__':
    unittest.main(exit=False)
