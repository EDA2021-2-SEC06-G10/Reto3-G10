#####-----#####-----#####-----#####-----#####   ##---####---##   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   MODIFICACIONES   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ##---####---##   #####-----#####-----#####-----#####-----#####

LUNES 1/11:
 1- Model: se definió la función new_sighting().
 2- Model: se modificó la función add_city().
 3- Controller: se modificó la función load_data() para cargar información a las estructuras 'city' y 'sightings'-
 4- Model: se creó la función add_sighting().
 5- View: se creó la función print_load_data().

MARTES 9/11:
 Model:
  1- Se modificó la función new_sighting() para cambiar a 'N.A.' los datos desconocidos.
  2- Se modificó la función add_city() para que las listas que contienen los avistamientos de cada ciudad sea arreglos y no listas enlazadas.
  3- Se definió la función de comapración cmp_by_datetime() del req. 1.
  4- Se actualizó la función new_catalog() para añadir al mapa 'latitude'.
  5- Se actualizó la función new_sighting() para que los datos 'longitude' y 'latitude' se añadieran como floats de dos decimales y el dato 'duration (seconds)' como int.
  6- Se definieron las funciones add_latitude() y add_longitude().
  7- Se definieron las funciones cmp_by_coordinates() y req_5() para el requerimiento 5.    
 View:
  1- Se modificó la función print_load_data() para que imprimiera la info. de interés de al momento de cargar.

MARTES 9/11:
 Model:
  1- Se modificó la función new_catalog() para añadir el mapa 'duration (seconds)'.
  2- Se definió la función cmp_by_city_country().
 Controller:
  1- Se definieron las funciones req_2() y req_5().
 View:
  1- Se modificó la función print_req_1().
  2- Se definió la función print_req_2().