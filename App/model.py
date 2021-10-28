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
        para llegar a la información requerida en tiempo constante.

        Es importante notar que todos los maps referencian a la misma información.
    
    """
    # Map cuyas llaves son años de nacimiento y cuyas llaves son listas enlazadas que contienen
    # información relevante de los artistas que nacieron el año correspondiente.
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
def add_city (catalog: dict, param_city: int) -> None:
    """
        

    """

    # Crear variable que guarda el mapa "BeginDate" del catálogo.
    map_city = catalog["city"]

    mp.put(map_city, param_city, 0)