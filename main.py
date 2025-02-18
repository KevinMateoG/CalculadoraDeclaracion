def tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony, rate):
    
   def tax_base():
     tax_base = gross_income - (costs_deductions + exempt_income)

   def tax_base_uvt():
       tax_base_uvt = tax_base / uvt_value
    
   def calculated_tax():
       calculated_tax = (tax_base*rate) - (tax_discounts+withholdings)
   
   def balance_favor():
      if calculated_tax < 0:
         return abs(calculated_tax)
      else:
         return 0

tax_payment()
