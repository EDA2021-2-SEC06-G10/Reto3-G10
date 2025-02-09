﻿"""
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
import datetime as dt
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



# Función que imprime la información relacionada a la carga de datos.
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
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('FECHA', 38), end = " # ")
    print(fixed_length('CIUDAD', 40), end = " # ")
    print(fixed_length('PAÍS', 8), end = " # ")
    print(fixed_length('FORMA', 30), end = " # ")
    print(fixed_length('DURACIÓN (S)', 14), end = " # ")
    print()
    print("#" * 147) 


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
    
    # Desempaquetar respuesta.
    size, lt_sight = ans_req_1
    
    # Respuesta tamaño.
    print('La base de datos tiene un resigtro de', size, 'avistamientos en la ciudad:', param_city + '.')
    
    # Lista.
    print('Una muestra de la información de algunos de estos avistamientos se dispone a continuación:\n')
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('FECHA', 38), end = " # ")
    print(fixed_length('CIUDAD', 40), end = " # ")
    print(fixed_length('PAÍS', 8), end = " # ")
    print(fixed_length('FORMA', 30), end = " # ")
    print(fixed_length('DURACIÓN (S)', 14), end = " # ")
    print()
    print("#" * 147) 

    # Si hay menos de 6 avistamientos.
    if (size < 6):
        for sighting in lt.iterator(lt_sight):
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        print("#" * 147)

    # Si hay 6 o más.
    else:
        for i in range(1,4):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        for i in range(size - 2, size + 1):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        print("#" * 147)
    print()



# Función que imprime la respuesta del requerimiento 2.
def print_req_2 (param_low: int, param_sup: int, ans_req_2: tuple) -> None:
    """
        Esta función imprime la respuesta del requerimiento 2 de una manera amigable para el usuario.

        Parámetros:
            -> param_low (int): límite inferior rango segundos.
            -> param_sup (int): límite superior rango segundos.
            -> ans_req_2 (tuple): tupla que contiene las respuestas del req.

        No tiene retorno.

    """
    
    # Desempaquetar respuesta.
    size, lt_sight = ans_req_2
    
    # Respuesta tamaño.
    print('La base de datos tiene un resigtro de', size, 'avistamientos cuyas duraciones tienen un valor entre', param_low, 'y', param_sup, 'segundos.')
    
    # Lista.
    print('Una muestra de la información de algunos de estos avistamientos se dispone a continuación:\n')
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('FECHA', 38), end = " # ")
    print(fixed_length('CIUDAD', 40), end = " # ")
    print(fixed_length('PAÍS', 8), end = " # ")
    print(fixed_length('FORMA', 30), end = " # ")
    print(fixed_length('DURACIÓN (S)', 14), end = " # ")
    print()
    print("#" * 147)

    # Si hay menos de 6 avistamientos.
    if (size < 6):
        for sighting in lt.iterator(lt_sight):
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        print("#" * 147)

    # Si hay 6 o más.
    else:
        for i in range(1,4):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        for i in range(size - 2, size + 1):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        print("#" * 147)
    print()



# Función que imprime la respuesta del requerimiento 4.
def print_req_4 (param_low: int, param_sup: int, ans_req_4: tuple) -> None:
    """
        Esta función imprime la respuesta del requerimiento 4 de una manera amigable para el usuario.

        Parámetros:
            -> param_low (int): límite inferior rango fechas.
            -> param_sup (int): límite superior rango fechas.
            -> ans_req_4 (tuple): tupla que contiene las respuestas del req.

        No tiene retorno.

    """
    
    # Desempaquetar respuesta.
    size, lt_sight = ans_req_4
    
    # Respuesta tamaño.
    print('La base de datos tiene un resigtro de', size, 'avistamientos que se registraron entre', param_low, 'y', str(param_sup) + '.')
    
    # Lista.
    print('Una muestra de la información de algunos de estos avistamientos se dispone a continuación:\n')
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('FECHA', 38), end = " # ")
    print(fixed_length('CIUDAD', 40), end = " # ")
    print(fixed_length('PAÍS', 8), end = " # ")
    print(fixed_length('FORMA', 30), end = " # ")
    print(fixed_length('DURACIÓN (S)', 14), end = " # ")
    print()
    print("#" * 147)

    # Si hay menos de 6 avistamientos.
    if (size < 6):
        for sighting in lt.iterator(lt_sight):
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        print("#" * 147)

    # Si hay 6 o más.
    else:
        for i in range(1,4):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        for i in range(size - 2, size + 1):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 38), end = " # ")
            print(fixed_length(sighting['city'], 40), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 30), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print()
        print("#" * 147)
    print()



# Función que imprime la respuesta del requerimiento 5.
def print_req_5 (mod_long_low: float, mod_long_sup: float , mod_lat_low: float , mod_lat_sup: float , ans_req_5: tuple) -> None:
    """
        Esta función imprime la respuesta del requerimiento 5 de una manera amigable para el usuario.

        Parámetros:
            -> mod_long_low (float): límite inferior longitud.
            -> mod_long_sup (float): límite inferior longitud.
            -> mod_lat_low (float): límite inferior latitud.
            -> mod_lat_sup (float): límite inferior latitud.
            -> ans_req_5 (tuple): tupla que contiene las respuestas del req.

        No tiene retorno.

    """
    
    # Desempaquetar respuesta.
    size, lt_sight = ans_req_5
    
    # Respuesta tamaño.
    print('La base de datos tiene un resigtro de', size, 'avistamientos que se registraron entre la latitud del rango', mod_lat_low, 'a', mod_lat_sup, 'y la longitud del rango', mod_long_low, 'a', str(mod_long_sup) + '.')
    
    # Lista.
    print('Una muestra de la información de algunos de estos avistamientos se dispone a continuación:\n')
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('FECHA', 25), end = " # ")
    print(fixed_length('CIUDAD', 25), end = " # ")
    print(fixed_length('PAÍS', 8), end = " # ")
    print(fixed_length('FORMA', 22), end = " # ")
    print(fixed_length('DURACIÓN (S)', 14), end = " # ")
    print(fixed_length('LATITUD', 15), end = " # ")
    print(fixed_length('LONGITUD', 15), end = " # ")
    print()
    print("#" * 147)

    # Si hay menos de 10 avistamientos.
    if (size < 10):
        for sighting in lt.iterator(lt_sight):
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 25), end = " # ")
            print(fixed_length(sighting['city'], 25), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 22), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print(fixed_length(sighting['latitude'], 15), end = " # ")
            print(fixed_length(sighting['longitude'], 15), end = " # ")
            print()
        print("#" * 147)

    # Si hay 10 o más.
    else:
        for i in range(1,6):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 25), end = " # ")
            print(fixed_length(sighting['city'], 25), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 22), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print(fixed_length(sighting['latitude'], 15), end = " # ")
            print(fixed_length(sighting['longitude'], 15), end = " # ")
            print()
        for i in range(size - 4, size + 1):
            sighting = lt.getElement(lt_sight, i)
            print("# ", end = " ")
            print(fixed_length(sighting['datetime'], 25), end = " # ")
            print(fixed_length(sighting['city'], 25), end = " # ")
            print(fixed_length(sighting['country'], 8), end = " # ")
            print(fixed_length(sighting['shape'], 22), end = " # ")
            print(fixed_length(sighting['duration (seconds)'], 14), end = " # ")
            print(fixed_length(sighting['latitude'], 15), end = " # ")
            print(fixed_length(sighting['longitude'], 15), end = " # ")
            print()
        print("#" * 147)
    print()




#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES CARGA DE DATOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán inicializar el catálogo de avistamiento y cargar
    los elementos de la base de datos.

"""

# Función que inicializa el catálogo.
def init_catalog () -> dict:
    """
        Inicializa el catálogo.

        No tiene parámtros.
        
        Retorno:
            -> (dict): el catálogo.

    """
    # Crear variable que guarda el catálogo y retornarlo.
    # Este se crea mediante la función homónima de controller.py.
    catalog = controller.init_catalog()
    return catalog



# Función que carga todos los datos al catálogo.
def load_data (catalog: dict) -> None:
    """
        Esta función carga todos los datos de interés de la carpeta Data/UFOS.

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
def fixed_length (input, lenght: int) -> str:
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
    
    # Volver el input una cadena de caracteres.
    text = str(input)

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

catalog = None       # Crear variable que guardará el catálogo.
os.system('cls')     # Limpiar la consola.

# Ciclo indefinido de la herramienta.
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
            print("""\n======================= Inputs Req. 1 =======================\n""")
                
            # Preguntar al usuario por la ciudad.
            param_city = input('Por favor, escriba la ciudad que desea consultar:\n  -> ')


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


        
        # Si escoge la opción 3.
        elif int(inputs[0]) == 3:

            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 2 =======================\n""")
                
            # Preguntar al usuario por inputs.
            param_low = input('Por favor, escriba el límite inferior del rango:\n  -> ')
            param_sup = input('Por favor, escriba el límite superior del rango:\n  -> ')

            # Convertir los inputs.
            int_param_low = int(float(param_low))
            int_param_sup = int(float(param_sup))


            # Si el input es válido.
            if (int_param_low < int_param_sup):

                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 2 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                ans_req_2 = controller.req_2(catalog, int_param_low, int_param_sup)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time) * 1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_2(param_low, param_sup, ans_req_2)


            # Si el input no es válido.
            else:
                
                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar un rango válido. Intente de nuevo.\n")
                sys.exit(0)
        


        # Si escoge la opción 4.
        elif int(inputs[0]) == 4:
            # Imprimir mensaje de error.
            os.system('cls')
            print("""\n======================= ERROR =======================\n""")
            print("Este requerimiento no fue realizado.\n\n")
            sys.exit(0)



        # Si escoge la opción 5.
        elif int(inputs[0]) == 5:

            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 4 =======================\n""")
                
            # Preguntar al usuario por por inputs.
            param_low = input('Por favor, escriba la fecha inferior del rango:\n  -> ')
            param_sup = input('Por favor, escriba la fecha superior del rango:\n  -> ')

            # Convertir los inputs.
            mod_param_low = dt.datetime.strptime(param_low, '%Y-%m-%d')
            mod_param_sup = dt.datetime.strptime(param_sup, '%Y-%m-%d')


            # Si el input es válido.
            if (mod_param_low < mod_param_sup):

                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 4 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                ans_req_4 = controller.req_4(catalog, param_low, param_sup)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time) * 1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_4(param_low, param_sup, ans_req_4)


            # Si el input no es válido.
            else:
                
                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar un rango válido. Intente de nuevo.\n")
                sys.exit(0)

        

        # Si escoge la opción 6.
        elif int(inputs[0]) == 6:

            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 5 =======================\n""")
                
            # Preguntar al usuario por inputs.
            lat_low = input('Por favor, escriba la latitud inferior del rango:\n  -> ')
            lat_sup = input('Por favor, escriba la latitud superior del rango:\n  -> ')
            long_low = input('Por favor, escriba la longitud inferior del rango:\n  -> ')
            long_sup = input('Por favor, escriba la longitud superior del rango:\n  -> ')

            # Convertir los inputs.
            mod_lat_low = float(lat_low)
            mod_lat_sup = float(lat_sup)
            mod_long_low = float(long_low)
            mod_long_sup = float(long_sup)


            # Si el input es válido.
            if (mod_lat_low < mod_lat_sup) and (mod_long_low < mod_long_sup):

                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 5 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                ans_req_5 = controller.req_5(catalog, mod_long_low, mod_long_sup, mod_lat_low, mod_lat_sup)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time) * 1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_5(mod_long_low, mod_long_sup, mod_lat_low, mod_lat_sup, ans_req_5)


            # Si el input no es válido.
            else:
                
                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar coordenadas válidas. Intente de nuevo.\n")
                sys.exit(0)



        # Opción salir.
        elif int(inputs[0]) == 0:
            
            # Limpiar la consola.
            os.system('cls')
            
            # Imprimir mensaje de carga.
            print("""\n======================= Exit =======================\n""")
            print("Gracias por usar la herramienta. Hasta pronto.\n\n")

            sys.exit(0)



        # Si se ingresa un valor erróneo.
        else:
            os.system('cls')        # Limpiar la consola.
            print("""\n======================= ERROR =======================\n""")
            print("Debe ingresar una opción válida.\n\n")
            sys.exit(0)



    # Si el usuario ingresó una opción inválida.
    except ValueError:
        os.system('cls')        # Limpiar la consola.
        print("""\n======================= ERROR =======================\n""")
        print("Debe ingresar valores adecuados.\n\n")
        sys.exit(0)

sys.exit(0)