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
    
        expected_result = 85_000_000, 1_806, 28, 22_300_000, 0

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
        
        self.assertAlmostEqual(calculated_tax, expected_result)
        
    def test_normal_2(self):
        uvt_value = 47065
        gross_income = 100_000_000
        costs_deductions = 0
        exempt_income = 0
        tax_discounts = 0
        withholdings = 1_000_000
        patrimony = 200_000_000

        expected_result = (100_000_000, 2_125, 28, 27_000_000, 0)

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)

        self.assertEqual(calculated_tax, expected_result)

    def test_normal_3(self):
        uvt_value = 47065
        gross_income = 69_718_000
        costs_deductions = 5_000_000
        exempt_income = 3_000_000
        tax_discounts = 500_000
        withholdings = 1_000_000
        patrimony = 80_000_000

        expected_result = (61_718_000, 1_311, 19, 10_226_420, 0)

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)

        self.assertEqual(calculated_tax, expected_result)

    def test_normal_4(self):
        uvt_value = 47065
        gross_income = 100_000_000
        costs_deductions = 95_000_000
        exempt_income = 0
        tax_discounts = 200_000
        withholdings = 300_000
        patrimony = 150_000_000

        expected_result = (5_000_000, 106, 0, -500_000, 1_000_000)

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)

        self.assertEqual(calculated_tax, expected_result)


    def test_extraordinary_1(self):
        uvt_value = 47065
        gross_income = 500_000_000
        costs_deductions = 50_000_000
        exempt_income = 10_000_000
        tax_discounts = 2_000_000
        withholdings = 5_000_000
        patrimony = 1_000_000_000
        
        expected_result = 440_000_000, 9_349, 35, 147_000_000, 0

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
            
        self.assertEqual(calculated_tax, expected_result)

    def test_extraordinary_2(self):
        uvt_value = 47065
        gross_income = 120_000_000
        costs_deductions = 50_000_000
        exempt_income = 20_000_000
        tax_discounts = 0
        withholdings = 500_000
        patrimony = 200_000_000

        expected_result = (50_000_000, 1_062, 0, -500_000, 1_000_000)

        calculated_tax = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
        
        self.assertEqual(calculated_tax, expected_result)

    def test_error_1(self):
        
        uvt_value = 47065
        gross_income = 1_000_000
        costs_deductions = 0
        exempt_income = -1_000_000
        tax_discounts = 0
        withholdings = 0
        patrimony = 1_000_000

        try:
            expected_result = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)

            self.fail("No sirvió bro")

        except main.ErrorRentaExenta as ex:
            pass

if __name__ == '__main__':
    unittest.main()
