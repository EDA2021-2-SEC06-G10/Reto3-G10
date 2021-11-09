"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

#####-----#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   IMPORTACIÓN MÓDULOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####-----#####

import os
import time
import config as cf
from DISClib.ADT import map as mp
import sys
import controller
from DISClib.ADT import list as lt
assert cf




#####-----#####-----#####-----#####-----#####-----#####   #####---######---#####   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES DE IMPRESIÓN   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   #####---######---#####   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán imprimir el menú y los resultados de cada
    requerimiento, de tal forma que se dispongan de una manera amigable para el usuario.

"""

# Función que imprime el menú de opciones.
def print_menu () -> None:
    """
        Esta función imprime el menú de interacción con el usuario. No tiene ni parámetros ni retorno.

    """
    
    print("""\n======================= BIENVENIDO =======================\n""")
    print("  1- Cargar información al catálogo.")
    print("  2- Cargar requerimiento 1.")
    print("  3- Cargar requerimiento 2.")
    print("  4- Cargar requerimiento 3.")
    print("  5- Cargar requerimiento 4.")
    print("  6- Cargar requerimiento 5.")



# Función que impre información relacionada a la carga de datos.
def print_load_data (lt_sightings: dict) -> None:
    """
        Dada la lista 'sightings' del catálogo, esta función imprime la información de los primeros
        y últimos 5 avistamientos encontrados en esta.

        Parámetro:
            -> lt_sightings (dict): lista con todos los avistamientos.

        No tiene retorno. 

    """
    
    lt_elemts = lt.newList('ARRAY_LIST')            # Lista avistamientos a imprimir.
    size_lt_sightings = lt.size(lt_sightings)       # Tamaño lista lt_sightings.

    # Añadir primeros cinco elementos.
    for pos in range(1,6):
        lt.addLast(lt_elemts, lt.getElement(lt_sightings, pos))
    
    # Añadir últimos cinco elementos.
    for pos in range(size_lt_sightings - 4, size_lt_sightings + 1):
        lt.addLast(lt_elemts, lt.getElement(lt_sightings, pos))

    # Imrpesión header.
    print('Una muestra de los primeros y últimos 5 avistamientos cargados se dispone a continuación:\n')
    print("#" * 148)
    print("# ", end = " ")
    print(fixed_length('FECHA', 38), end = " # ")
    print(fixed_length('CIUDAD', 40), end = " # ")
    print(fixed_length('PAÍS', 8), end = " # ")
    print(fixed_length('FORMA', 30), end = " # ")
    print(fixed_length('DURACIÓN (S)', 14), end = " # ")
    print()
    print("#" * 148) 


    # Impresión muestra primeros y últimos cinco avistamientos.
    for element in lt.iterator(lt_elemts):
        
        # Guardar infor. de interés del avistamiento actual en lista.
        date = element['datetime']
        city = element['city']
        country = element['country']
        shape = element['shape']
        duration= element['duration (seconds)']

        # Impresión datos avistamiento.
        print("# ", end = " ")
        print(fixed_length(date, 38), end = " # ")
        print(fixed_length(city, 40), end = " # ")
        print(fixed_length(country, 8), end = " # ")
        print(fixed_length(shape, 30), end = " # ")
        print(fixed_length(duration, 14), end = " # ")
        print()

    print("#" * 147)



# Función que imprime la respuesta del requerimiento 1.
def print_req_1 (param_city: str, ans_req_1: tuple) -> None:
    """
        Esta función imprime la respuesta del requerimiento 1 de una manera amigable para el usuario.

        Parámetros:
            -> param_city (str): ciudad a consultar.
            -> ans_req_1 (tuple): tupla que contiene las respuestas del req.

        No tiene retorno.

    """

    size, lt_sight = ans_req_1
    print(size)

    for i in range(1,4):
        elem = lt.getElement(lt_sight, i)
        print(elem['datetime'])

    for i in range(size - 2, size + 1):
        elem = lt.getElement(lt_sight, i)
        print(elem['datetime'])



#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES CARGA DE DATOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán inicializar el catálogo del museo y cargar
    los elementos de la base de datos.

"""

# Función que inicializa el catálogo del museo.
def init_catalog () -> dict:
    """
        Inicializa el catálogo del museo.

        No tiene parámtros.
        
        Retorno:
            -> (dict): el catálogo del museo.

    """
    # Crear variable que guarda el catálogo y retornarlo.
    # Este se crea mediante la función homónima de controller.py.
    catalog = controller.init_catalog()
    return catalog



# Función que carga todos los datos al catálogo.
def load_data (catalog: dict) -> None:
    """
        Esta función carga todos los datos de interés de la carpeta Data/MoMA.

        Parámetro:
            -> catalog (dict): catálogo.

        No tiene retorno.

    """
    # Cargar los datos mediante la función homónima de controller.py.
    controller.load_data(catalog)




#####-----#####-----#####-----#####-----#####-----#####   ####---#######---####   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES ADICIONALES   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ####---#######---####   #####-----#####-----#####-----#####-----#####-----#####

"""
    A continuación se definen funciones que serán de utilidad en general.

"""

# Función que permite acortar texto.
def fixed_length (text: str, lenght: int) -> str:
    """
        Dada una cadena de caracteres, esta función permite recotrarla en caso de que
        exceda la longitud necesario (especificada por el parámetro lenght), o adicionarle
        espacios en caso de no ser igual a la longitud necescaria.

        Parámetro:
            -> text (str): cadena que se desea recortar.
            -> lenght (int): longitud a la que se desea ajustar el texto.

        Retorno:
            -> (str): el texo ajustado a la longitud deseada.

    """
    
    # Si el texto excede lenght.
    if len(text) > lenght:
        text = text[:lenght -3] + '...'
    
    # Si el texto es menor que lenght.
    elif len(text) < lenght:
        text = (text + " " * lenght)[:lenght]

    # Retorno.
    return(text)




#####-----#####-----#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   MENÚ PRINCIPAL   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se define la iteración indefinida que permitirá al usuario cargar la información al catálogo y consultar los
    resultados de cada requerimiento. 

"""

# Crear variable que guardará el catálogo.
catalog = None

# Limpiar la consola.
os.system('cls')


# Iteración usuario.
while True:

    # Imprimir menú.
    print_menu()

    # Preguntar al usuario la acción que desea realizar.
    inputs = input('\nPor favor, seleccione una opción para continuar:\n  -> ')


    # Si el usuario ingresó una opción válida.
    try:
    
        # Opción carga de datos.
        if int(inputs[0]) == 1:

            # Limpiar la consola.
            os.system('cls')
            
            # Imprimir mensaje de carga.
            print("""\n======================= Carga de Datos =======================\n""")
            print("Cargando información al catálogo ...")

            catalog = init_catalog()            # Inicializar catálogo.
            start_time = time.process_time()    # Iniciar el tiempo
            load_data(catalog)                  # Cargar datos al catálogo.
            stop_time = time.process_time()     # Parar el tiempo.

            # Calcular tiempo de ejecución en milisegundos.
            elapsed_time_mseg = (stop_time - start_time)*1000

            lt_sightings = catalog['sightings']

            # Imprimir mensaje de éxito.
            print("\n<> Información cargada con éxito. <>")
            print("Tiempo de ejecución:", elapsed_time_mseg, "milisegundos.")
            print("\nEn total, la base de datos tiene un registro de", lt.size(lt_sightings), 'avistamientos.')
            print_load_data(lt_sightings)



        # Si escoge la opción 2.
        elif int(inputs[0]) == 2:

            # Limpiar la consola.
            os.system('cls')

            # Guardar mapa 'city'.
            mp_city = catalog['city']

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 2 =======================\n""")
                
            # Preguntar al usuario por la ciudad.
            param_city = input('Por favor, escriba la cidad que desea consultar:\n  -> ')

            # Determinar si el input es válido.
            mp.get(mp_city, param_city)


            # Si el input es válido.
            if not (mp.get(mp_city, param_city) == None):

                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 1 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                ans_req_1 = controller.req_1(catalog, param_city)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time) * 1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_1(param_city, ans_req_1)


            # Si el input no es válido.
            else:
                
                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar una ciudad que se encuentre en la base de datos. Intente de nuevo.\n")
                sys.exit(0)



        # Opción salir.
        elif int(inputs[0]) == 0:
            
            # Limpiar la consola.
            os.system('cls')
            
            # Imprimir mensaje de carga.
            print("""\n======================= Exit =======================\n""")
            print("Gracias por usar la herramienta. Hasta pronto.\n")

            sys.exit(0)



        # Si se ingresa un valor erróneo.
        else:
            print("""\n======================= ERROR =======================\n""")
            print("Debe ingresar una opción válida.\n\n")
            sys.exit(0)



    # Si el usuario ingresó una opción inválida.
    except ValueError:
        print("""\n======================= ERROR =======================\n""")
        print("Debe ingresar una opción válida.\n\n")
        sys.exit(0)

sys.exit(0)
