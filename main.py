def tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony, rate):
    tax_base = gross_income - (costs_deductions + exempt_income)
    tax_base_uvt = tax_base / uvt_value
    calculated_tax = (tax_base*rate) - (tax_discounts+withholdings)
    if calculated_tax < 0:
        return abs(calculated_tax)
    else:
        return 0
