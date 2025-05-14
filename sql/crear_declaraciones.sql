CREATE TABLE declaraciones(id_declaracion INT PRIMARY KEY,
                           valor_uvt decimal(9), 
                           ingresos_brutos decimal(100),
                           costos_deducciones decimal(100),
                           rentas_exentas decimal(100),
                           descuentos_tributarios decimal(100),
                           retenciones_fuente decimal(100),
                           patrimonio_neto decimal(100)
                          );
