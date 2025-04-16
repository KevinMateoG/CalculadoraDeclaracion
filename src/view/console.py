import sys
sys.path.append("src/model")  
from model.Logic_taxes import tax_payment

def calcular_impuesto():
    uvt_value = int(input("Ingrese el valor de la UVT: "))
    gross_income = int(input("Ingrese el ingreso bruto: "))
    costs_deductions = int(input("Ingrese los costos y deducciones: "))
    exempt_income = int(input("Ingrese la renta exenta: "))
    tax_discounts = int(input("Ingrese los descuentos tributarios: "))
    withholdings = int(input("Ingrese las retenciones: "))
    patrimony = int(input("Ingrese el patrimonio: "))

    try:
        result = main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
        print("Base Gravable:", result[0])
        print("Base Gravable en UVT:", result[1])
        print("Tarifa de Impuesto:", result[2], "%")
        print("Impuesto Calculado:", result[3])
        print("Balance a Favor:", result[4])
    except main.ErrorRentaExenta as ex:
        print("Error:", ex)
    except main.ErrorBaseGravable as ex:
        print("Error:", ex)

def verificar_errores():
    uvt_value = int(input("Ingrese el valor de la UVT: "))
    gross_income = int(input("Ingrese el ingreso bruto: "))
    costs_deductions = int(input("Ingrese los costos y deducciones: "))
    exempt_income = int(input("Ingrese la renta exenta: "))
    tax_discounts = int(input("Ingrese los descuentos tributarios: "))
    withholdings = int(input("Ingrese las retenciones: "))
    patrimony = int(input("Ingrese el patrimonio: "))

    try:
        main.tax_payment(uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony)
    except main.ErrorRentaExenta as ex:
        print("Error:", ex)
    except main.ErrorBaseGravable as ex:
        print("Error:", ex)

def main():
    while True:
        print("Menú Principal")
        print("1. Calcular Impuesto")
        print("2. Verificar Errores")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            calcular_impuesto()
        elif opcion == "2":
            verificar_errores()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 3.")

if __name__ == "__main__":
    main()