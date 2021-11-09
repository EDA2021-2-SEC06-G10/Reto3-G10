"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

import config as cf
import model
from DISClib.ADT import list as lt
import csv




#####-----#####-----#####-----#####-----#####   ##########-----###########-----##########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES INICIALIZACIÓN Y CARGA DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ##########-----###########-----##########   #####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán inicializar el catálogo del museo y cargar
    los elementos de la base de datos.

"""

# Función que inicializa y retorna el catálogo.
def init_catalog () -> dict:
    """
        Esta función invoca a la función nuevo_catalogo de model.py para crear y retornar al catálogo.

        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo. 

    """

    # Invocar función new_Catalog() de model.py, guardar su retorno en la variable catalog y retornarla.
    catalog = model.new_catalog()
    return catalog



# Función que carga toda la información al catálogo.
def load_data (catalog: dict) -> None:
    """
        Esta función carga toda la información al catálogo, y lo hace invocando a las 
        funciones load_artists() y load_artworks.

        Parámetro:
            -> catalog (dict): catálogo.

        No tiene retorno.

    """

    # Crear variable que guarda la referencia al archivo de los avistamientos y la que
    # guarda toda la información.
    file = cf.data_dir + '\\UFOS\\UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))


    # Iterar sobre cada avistamiento del catálogo.
    for sighting_info in input_file:
        
        sighting = model.new_sighting(sighting_info)    # Crear diccionario con la información del avistamiento.
        city = sighting['city']                         # Guardar su ciudad.

        # Añadirlo a la lista 'sightings'.
        model.add_sighting(catalog, sighting)

        # Añadirlo al mapa 'city'.
        model.add_city(catalog, city, sighting)




#####-----#####-----#####-----#####-----#####   ########-----#####-----########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES CONEXIÓN MODEL Y VIEW   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ########-----#####-----########   #####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán invocar las funciones referentes a
    la solución de los requerimientos, las cuales se encuentan en model.py.

"""

# Requerimiento 1.
def req_1 (catalog: dict, param_city: str) -> dict:
    """
        Dado el nombre de una ciudad, esta función retorna una tupla que contiene:
            1- Total de avistamientos de la ciudad.
            2- Arreglo que contiene los avistamientos de la ciudad ordenados cronológicamente.
        Esta función asume que param_city es una entrada válida.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_city (str): ciudad que se desea consultar.

        Retorno:
            -> (dict): tupla mencionada anteriormente.

    """
    
    # Invocar función del req. 1 y retornar su respuesta.
    ans_req_1 = model.req_1(catalog, param_city)
    return ans_req_1

'''
# Pruebas.
catalog = init_catalog()
load_data(catalog)

size, ltt = model.req_1(catalog, 'las vegas')
print(size)

for i in range(1,4):
    elem = lt.getElement(ltt, i)
    print(elem['datetime'])

for i in range(size - 2, size + 1):
    elem = lt.getElement(ltt, i)
    print(elem['datetime'])
'''