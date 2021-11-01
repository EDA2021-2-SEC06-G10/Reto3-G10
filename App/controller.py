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

    # Crear variable que guarda la referencia al archivo de los artistas.
    file = cf.data_dir + '\\UFOS\\UFOS-utf8-small.csv'

    # Crear variable que guarda todos los artistas.
    input_file = csv.DictReader(open(file, encoding='utf-8'))


    # Iterar sobre cada artista del catálogo.
    for sighting in input_file:
        city = sighting["city"]
        model.add_city(catalog, city)




#####-----#####-----#####-----#####-----#####   ########-----#####-----########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES CONEXIÓN MODEL Y VIEW   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ########-----#####-----########   #####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán invocar las funciones referentes a
    la solución de los requerimientos, las cuales se encuentan en model.py.

"""
