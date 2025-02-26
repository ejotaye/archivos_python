# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    archivo = open('stock.csv', 'r')
    stock = list(csv.DictReader(archivo))

    total_tornillos = 0

    for i in stock:
        total_tornillos += int(i['tornillos'])
    print('El total de tornillos es:', total_tornillos)

    archivo.close



def ej4():
    print('Ejercicios con archivos CSV 2º')

    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    
    try:
        archivo = open('propiedades.csv', 'r')
        propiedades = list(csv.DictReader(archivo))
        
        ambiente_2 = 0
        ambiente_3 = 0

        for i in propiedades:
            ambientes = i['ambientes']
            if ambientes == '2':
                ambiente_2 += 1
            if ambiente_3 == '3':
                ambiente_3 += 1        
        print('Departamentos con 2 ambientes:',ambiente_2)
        print('Departamentos con 3 ambientes:',ambiente_3)    
    except:
        print('No se encuentra el archivo') 

        archivo.close()

        #Profesor el ejercicio ej4() nose porque no me guarda los ambientes en las variables
        #intenté de muchas formas pero nada...



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
