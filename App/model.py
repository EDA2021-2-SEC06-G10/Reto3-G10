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
import datetime as dt
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qui
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
        Esta función permite crear la estructura de datos que guarda el catálogo de avistamientos.

        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo.

    """

    # Definir variable que guarda la información del catálogo e inicializar las variables que guardarán
    # las estructuras de datos que almacenarán la información.
    catalog = {}


    #####-----#####-----#####   Definición Listas   #####-----#####-----#####

    """
        A continuación se creará una lista que contendrá todos los avistamientos dentro de
        la base de datos.
    
    """
    catalog['sightings'] = lt.newList(datastructure = 'ARRAY_LIST')


    #####-----#####-----#####   Definición Maps/Índices   #####-----#####-----#####

    """
        A continuación se crearán maps por diferentes criterios
        para llegar a la información requerida en el menor tiempo posible.

        Es importante notar que todos los maps referencian a la misma información.
    
    """

    # Mapa desordenado cuyas llaves son ciudades en las que se han registrado avistamientos, y cuyos
    # valores son arreglos que contienen información relevante de los avistamientos registrados
    # en dicha ciudad.
    catalog["city"] = mp.newMap(80333, maptype='CHAINING', loadfactor = 4.0)

    # Mapa ordenado cuyas llaves son longitudes y cuyos valores son mapas ordenados.
    # Estos últimos tendrán como llaves latitudes y como valores listas enlazadas
    # que contendrán la información de los avistamientos que tienen dichas latitudes y longitudes.
    catalog['longitude'] = om.newMap('RBT')

    # Mapa ordenado cuyas llaves son duraciones en segundos y cuyos valores son listas enlazadas
    # que contienen los avistamientos que tienen dicha duración.
    catalog['duration (seconds)'] = om.newMap('RBT')

    # Mapa ordenado cuyas llaves son fechas de tipo YYYY-MM-DD y cuyos valores son listas enlazadas
    # que contienen los avistamientos que fueron registrados en dicha fecha.
    catalog['date'] = om.newMap('RBT')


    # Retorno.
    return catalog




#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ADICIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----######-----####-----#####

"""
    Se definen las funciones que permitirán añadir elementos al catálogo.

"""

# Función que agrega una avistamiento a la lista 'sightings' del catálogo.
def add_sighting (catalog: dict, sighting: dict) -> None:
    """
        Esta función permite agregar la información de un avistamiento a la lista 'sightings'
        del catálogo.

        Parámetros:
            -> catalog (dict): catálogo.
            -> sighting (dict): diccionario que representa al avistamiento que se quiere añadir.

        No tiene retorno.

    """

    # Guardar la lista y añadirle el avistamiento.
    lt_sightings = catalog['sightings']
    lt.addLast(lt_sightings, sighting)



# Función que agrega una pareja llave-valor al map "city".
def add_city (catalog: dict, param_city: str, sighting: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "city" del catálogo.
        
        La llave deberá ser una ciudad, es decir, una cadena de caracteres.
        El valor será un arreglo cuyos elementos son diccionarios que
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

    mp_city = catalog["city"]                   # Guardar el mapa 'city'.
    exists = mp.contains(mp_city, param_city)   # Determinar si la pareja llave-valor ya existe.

    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de los avistamientos que fueron registrados en param_city
        # y añadir a esta el avistamiento.
        lt_city_sigh = mp.get(mp_city, param_city)["value"]
        lt.addLast(lt_city_sigh, sighting)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de los avistamientos, añadir el avistamiento y añadir la pareja al map.
        new_lt_city_sigh = lt.newList('ARRAY_LIST')
        lt.addLast(new_lt_city_sigh, sighting)
        mp.put(mp_city, param_city, new_lt_city_sigh)



# Función que permite agregar parejas llave valor al mapa 'longitude'.
def add_longitude (catalog: dict, param_longitude: float, param_latitude: float , sighting: dict) -> None:
    """
        Dada la longitud de un avistamiento, esta función permite añadir una pareja longitude-om_latitude al RBT
        'longitude' del catálogo.

        La llave deberá ser una longitud, es decir, un número decimal.
        El valor será un árbol rojo-negro cuyos cuyas llaves serán latitudes y cuyos valores serán listas enlazadas
        que contienen los avistamientos que fueron registrados en la coordenada (param_longitude, param_latitude).
        Para más información acerca de dichos árboles, revisar la documentación de la función add_latitude().

        En caso de que la pareja longitude-om_latitude ya exista, se añadirá el avistamiento al om_latitude
        referente a param_longitude.
        En caso de que la pareja longitude-om_latitude no exista, se creará un nuevo om_latitude que contiene a los
        avistamientos reigistrados en la coordenada (param_longitude, param_latitude), se añadirá la información del 
        avistamiento a dicho árbol y se añadirá la nueva pareja longitude-om_latitude al map "longitude" del catálogo.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_longitude (float): longitud del avistaminto.
            -> param_latitude (float): latitud del avistaminto.
            -> sighting (dict): información del avistamiento.

        No tiene retornos.
    
    """

    om_longitude = catalog['longitude']             # Guardar mapa 'longitude'.
    exists = om.get(om_longitude, param_longitude)  # Determinar si la la llave param_longitude está en el mapa.

    # Si existe.
    if (exists):
        
        # Guardar el om_latitude y añadir la info. del avistamiento a dicho.
        om_latitude = om.get(om_longitude, param_longitude)['value']
        add_latitude(om_latitude, param_latitude, sighting)


    # De lo contrario.
    else:

        # Crear un nuevo om_latitude, añadir la pareja latitude-lt_sightings a dicho y añadir la pareja
        # longitude-om_latitude al mapa 'longitude'.
        new_om_latitude = om.newMap('RBT')
        add_latitude(new_om_latitude, param_latitude, sighting)
        om.put(om_longitude, param_longitude, new_om_latitude)



# Función que agrega una pareja llave-valor a los mapas om_latitude.
def add_latitude (om_latitude: dict, param_latitude: float, sighting: dict) -> None:
    """
        Esta función permite agregar parejas llave-valor a un mapa om_latitude. Estos se encuentran almacenados
        como valores de las parejas del mapa 'longitude' del catálogo.
        
        La llave deberá ser una latitud, es decir, un número decimal.
        El valor será una lista enlazada cuyos elementos son diccionarios que representan un avistamiento
        (para más detalle de qué información contienen estos diccionarios, revisar la documentación de la función 
        new_sighting()).

        En caso de que la pareja latitude-lt_sightings ya exista, se añadirá el avistamiento al lt_sightings.
        En caso de que la pareja latitude-lt_sightings no exista, se creará dicha lista, se añadirá la información
        del avistamiento a dicha lista y se añadirá la nueva pareja latitude-lt_sightings al map om_latitude respectivo.

        Parámetros:
            -> om_latitude (dict): mapa ordenado que contiene parejas latitude-lt_sightings.
            -> param_latitude (float): latitud del avistaminto.
            -> sighting (dict): información del avistamiento.

        No tiene retorno.

    """

    # Determinar si existe la llave param_latitude en om_latitude.
    exists = om.get(om_latitude, param_latitude)

    # Si existe.
    if (exists):

        # Guardar la lt_sightings y añadir el avistamiento a dicha.
        lt_sightings = om.get(om_latitude, param_latitude)['value']
        lt.addLast(lt_sightings, sighting)

    # De lo contrario.
    else:

        # Crear nuevo lt_sightings, añadir el avistamiento a dicha y añadir la pareja al om_latitude.
        new_lt_sightings = lt.newList('SINGLE_LINKED')
        lt.addLast(new_lt_sightings, sighting)
        om.put(om_latitude, param_latitude, new_lt_sightings)



# Función que agrega una pareja llave-valor al map "duration (seconds)".
def add_duration (catalog: dict, param_duration: int, sighting: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "duration (seconds)" del catálogo.
        
        La llave deberá ser una duración, es decir, un número entero.
        El valor será una lista enlazada cuyos elementos son diccionarios que
        representan un avistamiento (para más detalle de qué información contienen estos
        diccionarios, revisar la documentación de la función new_sighting()).

        En caso de que la pareja duration-sighting_list ya exista, se añadirá el avistamiento al sighting_list
        referente a la duración respectiva (la llave).
        En caso de que la pareja duration-sighting_list no exista, se creará la lista que contiene a los
        avistamientos de dicha duración, se añadirá la información del avistamiento a dicha lista
        y se añadirá la nueva pareja duration-sighting_list al map "duration (seconds)" del catálogo.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_duration (int): duración del avistamiento.
            -> sighting (dict): diccionario que representa al avistamiento que se quiere añadir.

        No tiene retorno.

    """

    om_duration = catalog["duration (seconds)"]         # Guardar el mapa 'duration (seconds)'.
    exists = om.contains(om_duration, param_duration)   # Determinar si la pareja llave-valor ya existe.

    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de los avistamientos de duración param_duration
        # y añadir a esta el avistamiento.
        lt_duration_sigh = om.get(om_duration, param_duration)["value"]
        lt.addLast(lt_duration_sigh, sighting)

    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de los avistamientos, añadir el avistamiento y añadir la pareja al map.
        new_lt_duration_sigh = lt.newList('ARRAY_LIST')
        lt.addLast(new_lt_duration_sigh, sighting)
        om.put(om_duration, param_duration, new_lt_duration_sigh)



# Función que agrega una pareja llave-valor al map 'date'.
def add_date (catalog: dict, param_date, sighting: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map 'date' del catálogo.
        
        La llave deberá ser una fecha de la forma YYYY-MM-DD, es decir, una cadena de caracteres.
        El valor será una lista enlazada cuyos elementos son diccionarios que
        representan un avistamiento (para más detalle de qué información contienen estos
        diccionarios, revisar la documentación de la función new_sighting()).

        En caso de que la pareja date-sighting_list ya exista, se añadirá el avistamiento al sighting_list
        referente a la fecha respectiva (la llave).
        En caso de que la pareja date-sighting_list no exista, se creará la lista que contiene a los
        avistamientos registrados en dicha fecha, se añadirá la información del avistamiento a dicha lista
        y se añadirá la nueva pareja date-sighting_list al mapa 'date' del catálogo.

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_date (str): fecha del avistamiento.
            -> sighting (dict): diccionario que representa al avistamiento que se quiere añadir.

        No tiene retorno.

    """

    om_date = catalog["date"]                                       # Guardar el mapa 'date'.
    mod_date = dt.datetime.strptime(param_date[0:10], '%Y-%m-%d')   # Guardar fecha modificada.
    exists = om.contains(om_date, mod_date)                         # Determinar si la pareja llave-valor ya existe.

    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de los avistamientos registrados en mod_date
        # y añadir a esta el avistamiento.
        lt_date_sigh = om.get(om_date, mod_date)["value"]
        lt.addLast(lt_date_sigh, sighting)

    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de los avistamientos, añadir el avistamiento y añadir la pareja al map.
        new_lt_date_sigh = lt.newList('SINGLE_LINKED')
        lt.addLast(new_lt_date_sigh, sighting)
        om.put(om_date, mod_date, new_lt_date_sigh)




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

    # Cambiar datos desconocidos a 'N.A.'.
    for key in sighting:
        if (sighting[key] == ''):
            sighting[key] = 'N.A.'
    
    # Convertir y apoximar duración, latitud y longitud a decimales de dos cifras.
    if not (sighting['duration (seconds)'] == 'N.A.'):
        sighting['duration (seconds)'] = int(float(sighting['duration (seconds)']))
    if not (sighting['latitude'] == 'N.A.'):
        sighting['latitude'] = round(float(sighting['latitude']), 2)
    if not (sighting['longitude'] == 'N.A.'):
        sighting['longitude'] = round(float(sighting['longitude']), 2)

    # Retornar el avistamiento.
    return sighting




#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES DE COMPARACIÓN   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones que permitirán comparar
    y ordenar los elementos del catálogo (incluyendo las llaves de los mapas).

"""

# Función de comparación del req. 1.
def cmp_by_datetime (sight_1: dict, sight_2: dict) -> bool:
    """
        Dada la infomación de dos avistamientos, esta función determina si el datetime del primero
        es menor que el del segundo.

        Parámetros:
            -> sight_1 (dict): info. primer avistamiento.
            -> sight_2 (dict): info. segundo avistamiento.

        Retorno:
            -> (bool): True si el datetime del primero avistamiento es menor que el del segundo.
                       False de lo contrario.
    
    """

    less_than = False               # Inicializar variable de retorno.
    dt_1 = sight_1['datetime']      # Fecha avistamiento 1.
    dt_2 = sight_2['datetime']      # Fecha avistamiento 2.

    # Asignar fechas por defecto si los avistamientos no tienen.
    if (dt_1 == 'N.A'):
        dt_1 = "0001-01-01 00:00:01"
    if (dt_2 == 'N.A'):
        dt_2 = "0001-01-01 00:00:01"

    # Crear variables con las fechas de adquisición modificadas.
    mod_dt_1 = dt.datetime.strptime(dt_1, '%Y-%m-%d %X')
    mod_dt_2 = dt.datetime.strptime(dt_2, '%Y-%m-%d %X')

    # Determinar si es menor y retornar.
    if (mod_dt_1 < mod_dt_2):
        less_than = True
    return less_than



# Función de comparación del req. 2.
def cmp_by_city_country (sight_1: dict, sight_2: dict) -> bool:
    """
        Dada la infomación de dos avistamientos, esta función determina si la combinación ciudad-país del primer
        avistamiento es alfabéticamente menor que la del segundo.

        Parámetros:
            -> sight_1 (dict): info. primer avistamiento.
            -> sight_2 (dict): info. segundo avistamiento.

        Retorno:
            -> (bool): True si se cumple la condición indicada.
                       False de lo contrario.
    
    """
    less_than = False               # Inicializar variable de retorno.

    # Determinar si se cumplen ambas condiciones estipuladas y retornar respuesta.
    city_less = (sight_1['city'] < sight_2['city'])
    country_less = (sight_1['country'] < sight_2['country'])
    less_than = (city_less and country_less)
    return less_than



# Función de comparación del req. 5.
def cmp_by_coordinates (sight_1: dict, sight_2: dict) -> bool:
    """
        Dada la infomación de dos avistamientos, esta función determina si tanto la latitud como la longitud
        de sight_1 son menores que la latitud y la longitud de sight_2 (respectivamente).

        Parámetros:
            -> sight_1 (dict): info. primer avistamiento.
            -> sight_2 (dict): info. segundo avistamiento.

        Retorno:
            -> (bool): True si se cumple la condición indicada.
                       False de lo contrario.
    
    """
    less_than = False               # Inicializar variable de retorno.

    # Determinar si se cumplen ambas condiciones estipuladas y retornar respuesta.
    latitude_less = (sight_1['latitude'] < sight_2['latitude'])
    longitude_less = (sight_1['longitude'] < sight_2['longitude'])
    less_than = True if (latitude_less and longitude_less) else False
    return less_than




#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES REQUERIMIENTOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones referentes a la implementación de
    los requerimientos.

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

    mp_city = catalog['city']                            # Guardar mapa 'city'.
    lt_sight = mp.get(mp_city, param_city)['value']      # Guardar arreglo avistamientos de la ciudad.

    # Determinar tamaño y ordenar lista avistamientos, empaquetarlos y retornar.
    size_lt_sight = lt.size(lt_sight)
    ord_lt_sight = mg.sort(lt_sight, cmp_by_datetime)
    return (size_lt_sight, ord_lt_sight)



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

    om_duration = catalog['duration (seconds)']        # Guardar mapa 'duration (seconds)'.
    lt_sight_return = lt.newList('ARRAY_LIST')         # Crear lista de retorno.

    # Crear variables que guardan el ceiling y el floor de las duraciones inferior y superior.
    min_duration = om.ceiling(om_duration, param_min_duration)
    max_duration = om.floor(om_duration, param_max_duration)

    # Recorrer todas las llaves del mapa 'duration (seconds)' que se encuentran dentro del rango.
    for duration in lt.iterator(om.keys(om_duration, min_duration, max_duration)):
        
        # Guardar lista de avistamientos de duration, ordenarla, iterarla y añadir todos sus elementos a lt_sight_return.
        lt_sightings = om.get(om_duration, duration)['value']
        ord_lt_sightings = qui.sort(lt_sightings, cmp_by_city_country)
        for sighting in lt.iterator(ord_lt_sightings):
            lt.addLast(lt_sight_return, sighting)

    # Ordenar la lista de retorno cronológicamente, determianr su tamaño, empaquetar y retornar.
    ordered_lt_sight_return = mg.sort(lt_sight_return, cmp_by_datetime)
    size_lt_sight_return = lt.size(ordered_lt_sight_return)
    return (size_lt_sight_return, ordered_lt_sight_return)



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

    om_date = catalog['date']                       # Guardar mapa 'date'.
    lt_sight_return = lt.newList('ARRAY_LIST')      # Crear lista de retorno.

    # Volver las fechas dadas por parámetro comparables.
    mod_min_date = dt.datetime.strptime(param_min_date, '%Y-%m-%d')
    mod_max_date = dt.datetime.strptime(param_max_date, '%Y-%m-%d')

    # Crear variables que guardan el ceiling y el floor de las fechas inferior y superior.
    min_date = om.ceiling(om_date, mod_min_date)
    max_date = om.floor(om_date, mod_max_date)

    # Recorrer todas las llaves del mapa 'date' que se encuentran dentro del rango.
    for date in lt.iterator(om.keys(om_date, min_date, max_date)):
        
        # Guardar lista de avistamientos en date, iterarla y añadir todos sus elementos a lt_sight_return.
        lt_sightings = om.get(om_date, date)['value']
        for sighting in lt.iterator(lt_sightings):
            lt.addLast(lt_sight_return, sighting)

    # Determianr tamaño lt_sight_return, empaquetar y retornar.
    size_lt_sight_return = lt.size(lt_sight_return)
    return (size_lt_sight_return, lt_sight_return)



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

    om_longitude = catalog['longitude']         # Guardar mapa 'longitude'.
    return_list = lt.newList('ARRAY_LIST')      # Crear lista de retorno.

    # Crear variables que guardan el ceiling y el floor de las longitudes inferior y superior.
    floor_long = om.ceiling(om_longitude, min_long)
    ceil_long = om.floor(om_longitude, max_long)


    # Crear iterador del rango [floor_long, ceil_long] e iterar sobre este.
    iterator_long = lt.iterator(om.keys(om_longitude, floor_long, ceil_long))
    for longitude in iterator_long:

        # Determinar si existe la llave longitude en om_longitude.
        exists = om.get(om_longitude, longitude)


        # Si existe la pareja longitude-om_latitude en om_longitude.
        if (exists):

            # Guardar el om_latitude de longitude, crear su iterador e iterar sobre este.
            om_latitude = om.get(om_longitude, longitude)['value']
            iterator_om_latitude = lt.iterator(om.keys(om_latitude, om.minKey(om_latitude), om.maxKey(om_latitude)))
            for latitude in iterator_om_latitude:
                
                # Determinar si latitud está entre el rango [min_lat, max_lat].
                valid = (latitude >= min_lat and latitude <= max_lat)

                # Si es válido.
                if (valid):
                    # Guardar lt_sightings, recorrerla y añadir cada avistamiento a return_list.
                    lt_sightings = om.get(om_latitude, latitude)['value']
                    for element in (lt.iterator(lt_sightings)):
                        lt.addLast(return_list, element)

        
    # Determinar tamaño, empaquetar variables y retornar.
    size_return_list = lt.size(return_list)
    return(size_return_list, return_list)