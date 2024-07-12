import random as rd
import csv
import statistics
import Funciones as fn

trabajadores = [
    "Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"
    ]

sueldo_trabajador = {}

def asignar_sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldo = rd.randint(300000,2500000)
        sueldo_trabajador[trabajadores] = sueldo
        print(sueldo_trabajador)
    return(trabajador)


def clasificar_sueldos():
    sueldo_menor = []
    sueldo_entre = []
    sueldo_superior = []
    total_menor = 0
    total_entre = 0
    total_superior = 0

    for trabajador in trabajadores:
        if sueldo_trabajador > 800000:
            sueldo_menor.append(trabajador)
            total_menor == total_menor + 1
        else:
            if sueldo_trabajador > 800001 and sueldo_trabajador < 2000000:
                sueldo_entre.append(trabajador)
                total_entre == total_entre + 1
            else:
                if sueldo_trabajador > 2000000:
                    sueldo_superior.append(trabajador)
                    total_superior == total_superior + 1
    
        print("Sueldos menores a $800.000 son: ", total_menor)
        print(sueldo_menor)
        print("Sueldos entre $800.000 y $2.000.000 son: ",total_entre)
        print(sueldo_entre)
        print("Sueldos superiores a $2.000.000 son: ",total_superior)
        print(sueldo_superior)

def ver_estadisticas():
    print("estadistica")

def reporte_sueldo():
    print("reporte")