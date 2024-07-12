"""
Lista de trabajadores y sueldos
- 10 sueldos de empleados
- entre $300.000 y $2.500.000
"""
import Funciones as fn
import random as rd

trabajadores = [
    "Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"
    
    ]

#iniciar trabajadores
#trabajador = 0
#for trabajador in trabajadores:


#MENU
while True:
    try:
        print("Bienvenido a analisis de datos\n")
        print("Por favor seleccione una opcion del menu: ")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Escriba la opcion a la que desea ingresar: "))
    

        if opcion == 1:
            print("Usted ha seleccionado asignar sueldos aleatoriamente")
            fn.asignar_sueldos_aleatorios
            
        elif opcion == 2:
            print("Usted ha seleccionado clasificar sueldos")
            fn.clasificar_sueldos
            

        elif opcion == 3:
            print("Usted ha seleccionado ver estadisticas")
            fn.ver_estadisticas
            
        elif opcion == 4:
            print("Usted ha seleccionado realizar reporte")
            fn.reporte_sueldo
            
        
        elif opcion == 5:
            print("Finalizando el programa...")
            print("Desarrollado por Diego Cabrera")
            print("Rut 19.872.688-5")
    
    
    except:
        print("Favor ingrese una opcion valida!")