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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   IMPORTACIÓN MÓDULOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf




#####-----#####-----#####-----#####-----#####   ########-----######-----########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   DEFINICIÓN ESTRUCTURAS ELEMENTOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ########-----######-----########   #####-----#####-----#####-----#####-----#####

"""
    Se define la estructura que contiene el catálogo de videos.
    El catálogo tendrá dos listas, una para los videos y otra para 
    las categorias de dichos.

"""

# Función que crea y retorna el catálogo.
def new_catalog () -> dict:
    """
        Esta función permite crear la estructura de datos que guarda el catálogo de videos.
        Esta está compuesta por los siguientes maps:
            1- city (unordered_map)

        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo del museo.

    """

    # Definir variable que guarda la información del catálogo e inicializar las variables que guardarán
    # las estructuras de datos que almacenarán la información.
    catalog = {"city": None}



    #####-----#####-----#####   Definición Maps/Índices   #####-----#####-----#####

    """
        A continuación se crearán maps por diferentes criterios
        para llegar a la información requerida en el menor tiempo posible.

        Es importante notar que todos los maps referencian a la misma información.
    
    """

    # Mapa desordenado cuyas llaves son ciudades en las que se han registrado avistamientos, y cuyos
    # valores son listas enlazadas que contienen información relevante de los avistamientos registrados
    # en dicha ciudad.
    catalog["city"] = mp.newMap(80333, maptype='CHAINING', loadfactor = 4.0)



    # Retorno.
    return catalog




#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ADICIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----######-----####-----#####

"""
    Se definen las funciones que permitirán añadir elementos al catálogo.

"""

# Función que agrega una pareja llave-valor al map "city".
def add_city (catalog: dict, param_city: str, sighting: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "city" del catálogo.
        
        La llave deberá ser una ciudad, es decir, una cadena de caracteres.
        El valor será una lista enlazada, cuyos elementos son diccionarios que
        representan un avistamiento (para más detalle de qué información contienen estos
        diccionarios, revisar la documentación de la función new_sighting()).

        En caso de que la pareja city-sighting_list ya exista, se añadirá el avistamiento al sighting_list
        referente a la ciudad respectiva (la llave).
        En caso de que la pareja city-sighting_list no exista, se creará la lista que contiene a los
        avistamientos reigistrados en city, se añadirá la información del avistamiento a dicha lista
        y se añadirá la nueva pareja city-sighting_list al map "city" del catálogo.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_city (str): ciudad del avistamiento.
            -> sighting (dict): diccionario que representa al avistamiento que se quiere añadir.

        No tiene retorno.

    """

    mp_city = catalog["city"]          # Guardar el mapa 'city'.

    # Determinar si la pareja llave-valor ya existe.
    exists = mp.contains(mp_city, param_city)


    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de los avistamientos que fueron registrados en param_city.
        lt_city_sigh = mp.get(mp_city, param_city)["value"]

        # Añade el avistamiento a lt_city_sigh.
        lt.addLast(lt_city_sigh, sighting)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de los avistamientos.
        new_lt_city_sigh = lt.newList('SINGLE_LINKED')
        
        # Añade el avistamiento a new_lt_city_sigh.
        lt.addLast(new_lt_city_sigh, sighting)

        # Añade la pareja city-lt_city_sigh al map.
        mp.put(mp_city, param_city, new_lt_city_sigh)    
    



#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES DE COMPARACIÓN   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones que permitirán comparar
    y ordenar los elementos del catálogo (incluyendo las llaves de los maps).

"""





#####-----#####-----#####-----#####-----#####   ###---####----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   CREACIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---####----###   #####-----#####-----######-----####-----#####

"""
    Se define las funciones que permitirán crear elementos referentes a información
    de interés del catálogo.

"""

# Función que crea un avistamiento.
def new_sighting (sighting_info: dict) -> dict:
    """
        Esta función permite crear un diccionario que almacenará la información de interés de un avistamiento.
        Estos se representarán mediante el tipo de dato dict de Python.

        Parámetros:
            -> sighting_info (dict): diccionario que tiene toda la información de interés del avistamiento.

        Retorno:
            -> (dict): diccionario que representa al avistamiento.

    """

    # Crear variable que guardará el diccionario del avistamiento.
    sighting = {}

    # Añadir los datos de interés.
    sighting['datetime'] = sighting_info['datetime']
    sighting['city'] = sighting_info['city']
    sighting['state'] = sighting_info['state']
    sighting['country'] = sighting_info['country']
    sighting['shape'] = sighting_info['shape']
    sighting['duration (seconds)'] = sighting_info['duration (seconds)']
    sighting['duration (hours/min)'] = sighting_info['duration (hours/min)']
    sighting['comments'] = sighting_info['comments']
    sighting['date posted'] = sighting_info['date posted']
    sighting['latitude'] = sighting_info['latitude']
    sighting['longitude'] = sighting_info['longitude']

    # Retornar el avistamiento.
    return sighting




#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES DE COMPARACIÓN   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones que permitirán comparar
    y ordenar los elementos del catálogo (incluyendo las llaves de los maps).

"""





#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES REQUERIMIENTOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones referentes a la implementación de
    los requerimientos.

"""





#####-----#####-----#####-----#####-----#####   #####---####----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES ADICIONALES   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---####----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen funciones que serán necesarias para desarrollar los
    requerimientos, o que serán de utilidad en general.

"""
