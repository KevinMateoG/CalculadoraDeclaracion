def tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony):
    # Calcular Base Gravable
    tax_base = gross_income - costs_deductions - exempt_income
    tax_base_uvt = tax_base / uvt_value if uvt_value else 0
    
    # Determinar tarifa según la base gravable en UVT (esto puede ajustarse según normativa específica)
    if tax_base_uvt <= 0:
        rate = 0.0
    elif tax_base_uvt < 1000:
        rate = 0.19
    elif tax_base_uvt < 5000:
        rate = 0.28
    else:
        rate = 0.35
    
    # Calcular impuesto
    calculated_tax = (tax_base * rate) - (tax_discounts + withholdings)
    
    # Determinar saldo a favor
    balance_favor = max(0, withholdings + tax_discounts - calculated_tax)

    rate = rate*100
    
    return round(tax_base), round(tax_base_uvt), round(rate), round(calculated_tax), round(balance_favor)
