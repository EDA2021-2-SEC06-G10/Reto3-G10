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
    Se definen las funciones que permitirán inicializar el catálogo y cargar
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
        Esta función carga toda la información al catálogo.

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
        duration = sighting['duration (seconds)']       # Guardar su duración en segundos.
        longitude = sighting['longitude']               # Guardar su longitud.
        latitude = sighting['latitude']                 # Guardar su latitud.
        date = sighting['datetime']                     # Guardar su fecha.
        
        model.add_sighting(catalog, sighting)                        # Añadirlo a la lista 'sightings'.
        model.add_city(catalog, city, sighting)                      # Añadirlo al mapa 'city'.
        model.add_duration(catalog, duration, sighting)              # Añadirlo al map 'duration (seconds)'.
        model.add_longitude(catalog, longitude, latitude, sighting)  # Añadirlo al map 'longitud'.
        model.add_date(catalog, date, sighting)                      # Añadirlo al map 'date'.




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



# Requerimiento 2.
def req_2 (catalog: dict, param_min_duration: int, param_max_duration: int) -> tuple:
    """
        Dado un rango de segundos, esta función retorna una tupla que contiene un arreglo que almacena los avistamientos
        cuya duración en segundos se encuentra dentro de dicho rango y su tamaño.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_min_duration (int): límite inferior rango duración.
            -> param_max_duration (int): límite superior rango duración.

        Retorno:
            -> (tuple): tupla con los elementos mencionados.
    
    """
    # Invocar función del req. 2 y retornar su respuesta.
    ans_req_2 = model.req_2(catalog, param_min_duration, param_max_duration)
    return ans_req_2



# Requerimiento 4.
def req_4 (catalog: dict, param_min_date: str, param_max_date: str) -> tuple:
    """
        Dado un rango de fechas, esta función retorna una tupla que contiene un arreglo que almacena los avistamientos
        que fueron registrados entre dicho rango y su tamaño.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_min_date (str): límite inferior rango fechas.
            -> param_max_date (str): límite superior rango fechas.

        Retorno:
            -> (tuple): tupla con los elementos mencionados.
    
    """
    # Invocar función del req. 4 y retornar su respuesta.
    ans_req_4 = model.req_4(catalog, param_min_date, param_max_date)
    return ans_req_4



# Requerimiento 5.
def req_5 (catalog: dict, min_long: float, max_long: float, min_lat: float, max_lat: float) -> tuple:
    """
        Dada una zona geográfica definida por un rango de longitudes y latitudes, esta función retorna una tupla
        que contiene un arreglo que contiene los avistamientos que se registraron en dentro de dicha zona y su tamaño.

        Esta función asume que el rango de longitudes y latitudes es válido.

        Parámetros:
            -> catalog (dict): catálogo.
            -> min_long (float): límite mínimo de longitud.
            -> max_long (float): límite máximo de longitud.
            -> min_lat (float): límite mínimo de latitud.
            -> max_lat (float): límite máximo de latitud.

        Retorno:
            -> (tuple): tupla con los elementos mencionados.
    
    """
    # Invocar función del req. 5 y retornar su respuesta.
    ans_req_5 = model.req_5(catalog, min_long, max_long, min_lat, max_lat)
    return ans_req_5