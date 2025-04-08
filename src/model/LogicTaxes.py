class ErrorRentaExenta(Exception):
    """ ERROR: La renta exenta no puede ser negativa """

class ErrorBaseGravable(Exception):
    """ ERROR: La Base Gravable no puede ser negativa """

class ErrorIngresoBruto(Exception):
    """ERROR: No se puede tener un ingreso bruto igual a 0"""


def tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony):

    if exempt_income < 0:
        raise ErrorRentaExenta()
    
    if gross_income == 0:
        raise ErrorBaseGravable

# Cálculo de la base gravable
    tax_base = gross_income - costs_deductions - exempt_income
    tax_base_uvt = tax_base / uvt_value if uvt_value else 0

    if tax_base < 0:
        raise ErrorBaseGravable()

# Cálculo de la tarifa basándonos en la base gravable en UVT (Unidad de Valor Tributario)
    if tax_base_uvt <= 1090:
        rate = 0.0
    elif tax_base_uvt <= 1700:
        rate = 0.19
    elif tax_base_uvt <= 4100:
        rate = 0.28
    elif tax_base_uvt <= 8670:
        rate = 0.33
    elif tax_base_uvt <= 18970:
        rate = 0.35
    elif tax_base_uvt <= 31000:
        rate = 0.37
    else:
        rate = 0.39
    
    calculated_tax = (tax_base * rate) - (tax_discounts + withholdings)
    
    balance_favor = max(0, withholdings + tax_discounts - calculated_tax)

    rate = rate*100
    
    return round(tax_base), round(tax_base_uvt), round(rate), round(calculated_tax), round(balance_favor)
