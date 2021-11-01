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

            # Inicializar catálogo.
            catalog = init_catalog()

            # Iniciar el tiempo.
            start_time = time.process_time()

            # Cargar datos al catálogo.
            load_data(catalog)

            # Parar el tiempo.
            stop_time = time.process_time()

            # Calcular tiempo de ejecución en milisegundos.
            elapsed_time_mseg = (stop_time - start_time)*1000

            # Imprimir mensaje de éxito.
            print("\n<> Información cargada con éxito. <>")
            print("Tiempo de ejecución:", elapsed_time_mseg, "milisegundos.")
            print("En total hay", mp.size(catalog['city']), "ciudades en las que hubo avistamientos.")


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
