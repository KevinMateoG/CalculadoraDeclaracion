# PROYECTO CALCULADORA DE IMPUESTO A PAGAR DE DECLARACIÓN DE RENTA 
# by Cristian David Toro Arboleda & Pedro Hernández

## VARIABLES DE ENTRADA Y SALIDA

**VARIABLES DE ENTRADA**
-	Ingresos Brutos
-	Costos y Gastos Deducibles
-	Rentas Exentas
-	Descuentos Tributarios
-	Retenciones en la Fuente
-	Patrimonio
-	Valor del UVT (Año cerrad)
    (Unidad de Valor Tributario, valor propio de la DIAN para la declaración de renta)
    
  
**VARIABLES DE SALIDA**
-	Base Gravable
-	Impuesto a pagar
-	Saldo a favor (Si aplica)

## Audio con el experto
Link de Drive: https://drive.google.com/file/d/15PLIftSmdbX2hj9vXdWDiRgb2k7XdemK/view?usp=sharing

# Explicación del código

## Arquitectura del código

El código cuenta con una estructura de carpetas descritas en las bases del Código Limpio donde tenemos dos carpeta raíces "src" y "tes" y varias carpetas adyacentes a src las cuales son model (donde va la lógica del programa) y view (donde va la interfaz del programa)

**main**
En el archivo main.py tenemos la lógica básica de la calculadora del impuesto donde hacemos cálculos básicos para conseguir todos los datos necesarios a partir de los datos ingresados en la interfaz por consola o en las pruebas unitarias.

**test**
En el archivo test.py tenemos todas las pruebas unitarias donde contenemos 4 pruebas normales, 2 pruebas extraordinarias y 2 pruebas de error, la librería utilizada para las pruebas unitarias fue aquella de Python llamada "Unittest" donde se compara un resultado esperado con el resultado que arroje la lógica del programa.

## ¿Cómo ejecutar las pruebas?
Es tan sencillo como simplemente tener el proyecto clonado y abierto en Visual Studio Code y usar la función de TESTING incorporada.



