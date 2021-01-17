"""

Programa para obtener de la API de la AEMET, aprovechando para ello un modulo que existe
en GitHub, los datos de las temperaturas mínimas y máximas, junto con su correspondiente 
hora para un rango de fechas dado, para las estaciones de las provincias que se indiquen.

Previamente a su ejecución hay que instalar con pip este mencionado módulo.

https://opendata.aemet.es/centrodedescargas/inicio
https://github.com/pablo-moreno/python-aemet

"""

##########################################################################################
#                                                                                        #
#                                                                                        #
#                       I M P O R T S  / C O N S T A N T E S                             #
#                                                                                        #
#                                                                                        #
##########################################################################################
#Importar sólo las clases del modulo de AEMET que se van a utilizar
from aemet import Aemet, Estacion
import json
import datetime 

#Constantes para la API_KEY de AEMET y para las provincias a consultar
AEMET_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhMjBzYW5ydWJqMDQzM0BpZXMtbWFyZGVjYWRpei5jb20iLCJqdGkiOiIxZGNhMjhmYS02MWFhLTQ2YTEtYWM5NS1kMTM5NWRjMDc1YjYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTYxMDcwNTU5NiwidXNlcklkIjoiMWRjYTI4ZmEtNjFhYS00NmExLWFjOTUtZDEzOTVkYzA3NWI2Iiwicm9sZSI6IiJ9.mAsykwB_ERJXD6L2MY6N4OnBkpMxV7GbS5oMHaQncnw"
#PROVINCIAS = ("CADIZ", "HUELVA", "SEVILLA", "CORDOBA", "GRANADA", "MALAGA", "JAEN", "ALMERIA")
#PROVINCIAS = ("CADIZ", "HUELVA", "SEVILLA")
PROVINCIAS = ("LEON", "VALLADOLID", "ALBACETE")

#Constantes para el rango de fechas a consultar de la API de la AEMET
FECHA_INICIO = "2021-01-01"
FECHA_FIN    = "2021-01-15"
#FECHA_FIN = str(datetime.datetime.now())[:10]


##########################################################################################
#                                                                                        #
#                                                                                        #
#                               F U N C I O N E S                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################
### -------------------------------------------------- main() -------------------------------------------------- ###
#Función principal
def main():
    #Variables necesarias para consultar la API (No se cómo crear un datetime con el formato "AAAA-MM-DDTHH:MM:SSUTC")
    fecha_inicio = FECHA_INICIO + "T00:00:00UTC"
    fecha_fin    = FECHA_FIN    + "T23:59:59UTC"

    datos_temperaturas = []

    #Se instancia la clase Aemet, pasándole la API KEY
    aemet = Aemet(AEMET_API_KEY)

    #Se consultan todas las estaciones para poder recorrerlas posteriormente,
    #ya que para obtener las valores climatológicos diarios es necesario el indicativo de la estación
    estaciones = Estacion.get_estaciones(AEMET_API_KEY)

    #Se recorren las estaciones
    for estacion in estaciones:
        #Sólo se toman las que nos interesan
        if estacion["provincia"] in PROVINCIAS:
            #print("Provincia: {} Indicativo: {} Nombre: {}".format(estacion["provincia"], estacion["indicativo"], estacion["nombre"]))
            valores_climatologicos_diarios = aemet.get_valores_climatologicos_diarios(fecha_inicio, fecha_fin, estacion["indicativo"])

            #No hay datos para esa estación en el rango de fechas que se ha pasado
            if isinstance(valores_climatologicos_diarios, dict) and "estado" in valores_climatologicos_diarios:
                mostrar_no_hay_datos_estacion_en_rango_fechas(valores_climatologicos_diarios, estacion, FECHA_INICIO, FECHA_FIN)
            else:
                #Recorrer lista para coger de cada entrada los valores que interesan
                for valor_climatologico_diario in valores_climatologicos_diarios:
                    #mostrar_datos_estacion_dia(estacion, valor_climatologico_diario)

                    datos_temperaturas.append(obtener_registro_temperaturas(estacion, valor_climatologico_diario, datos_temperaturas))

    #Una vez se tienen todos los datos de las estaciones, se muestran o se salvan
    procesar_datos_temperaturas(datos_temperaturas)

    #Si ha habido datos, se procesan para obtener la mínima y la máxima de cada provincia por día
    if datos_temperaturas:
        datos_minimas_maximas_temperaturas = obtener_minima_maxima_por_dia_y_provincia(datos_temperaturas[:])

        mostrar_datos_minimas_maximas_temperaturas(datos_minimas_maximas_temperaturas)
    else:
        print("No hay datos de temperaturas para {} en las fechas {}-{}".format(PROVINCIAS, FECHA_INICIO, FECHA_FIN))


### -------------------------------------------------- obtener_registro_temperaturas() -------------------------------------------------- ###
#Función para devolver un diccionario con los datos para hacer un registro de temperatura
def obtener_registro_temperaturas(estacion, valor_climatologico_diario, datos_temperaturas):
    provincia = estacion["provincia"] if "provincia" in estacion else None
    nombre    = estacion["nombre"]    if "nombre"    in estacion else None
    
    fecha    = valor_climatologico_diario["fecha"]    if "fecha"    in valor_climatologico_diario else None
    tmin     = valor_climatologico_diario["tmin"]     if "tmin"     in valor_climatologico_diario else None
    horatmin = valor_climatologico_diario["horatmin"] if "horatmin" in valor_climatologico_diario else None
    tmax     = valor_climatologico_diario["tmax"]     if "tmax"     in valor_climatologico_diario else None
    horatmax = valor_climatologico_diario["horatmax"] if "horatmax" in valor_climatologico_diario else None

    registro_temperaturas = {
        "provincia":   provincia,
        "nombre":      nombre,
        "fecha":       fecha,
        "minima":      tmin,
        "hora_minima": horatmin,
        "maxima":      tmax,
        "hora_maxima": horatmax
    }

    return registro_temperaturas




### -------------------------------------------------- mostrar_datos_estacion_dia() -------------------------------------------------- ###
#Función para mostrar los datos de una estación en un determinado día
#con su temperatura mínima y máxima, indicando la hora en que ocurrió
def mostrar_datos_estacion_dia(estacion, valor_climatologico_diario):
    print("Provincia: {:20} Nombre: {:40} Fecha: {} Mínima: {:>5} HoraMin: {:10} Máxima: {:>5} HoraMax: {:10}".format(\
        estacion["provincia"], \
        estacion["nombre"],  \
        valor_climatologico_diario["fecha"], \
        valor_climatologico_diario["tmin"], \
        valor_climatologico_diario["horatmin"], \
        valor_climatologico_diario["tmax"], \
        valor_climatologico_diario["horatmax"]  ))




### -------------------------------------------------- procesar_datos_temperaturas() -------------------------------------------------- ###
#Mostrar y/o grabar en fichero los datos de temperaturas que se han obtenido
def procesar_datos_temperaturas(datos_temperaturas):
    if not datos_temperaturas:
        print("No hay datos para NINGUNA estación entre las fechas {} y {}.".format(FECHA_INICIO, FECHA_FIN))
    else:
        #print(json.dumps(datos_temperaturas, ensure_ascii=False, indent=2)).encode("utf8")

        with open("datos_temperaturas", "w", encoding="utf-8") as fichero:
            json.dump(datos_temperaturas, fichero, ensure_ascii=False, indent=4)



### -------------------------------------------------- mostrar_no_hay_datos_estacion_en_rango_fechas() -------------------------------------------------- ###
#Mostrar que no hay datos para esa estación en el rango de fechas que se ha pasado
def mostrar_no_hay_datos_estacion_en_rango_fechas(valores_climatologicos_diarios, estacion, fecha_inicio, fecha_fin):
    print("No hay datos de temperaturas entre el {} y el {}, para la estación {} de la pronvincia de {}, ubicada en {}.".format(\
        fecha_inicio, \
        fecha_fin, \
        estacion["indicativo"], \
        estacion["provincia"], \
        estacion["nombre"],))




### -------------------------------------------------- obtener_minima_maxima_por_dia_y_provincia() -------------------------------------------------- ###
#Obtener la temperatura mímina y máxima con sus correspondientes horas para el rango de fechas dadas para las estaciones consultadas
def obtener_minima_maxima_por_dia_y_provincia(datos_temperaturas):
    datos_minimas_maximas_temperaturas = []

    #Recorrer la lista para procesar cada entrada
    for dato_temperaturas in datos_temperaturas:
        #Se guardan los valores que se quieren utilizar en variables
        provincia = dato_temperaturas["provincia"]
        fecha     = dato_temperaturas["fecha"]
        tmin      = dato_temperaturas["minima"]
        horatmin  = dato_temperaturas["hora_minima"]
        tmax      = dato_temperaturas["maxima"]
        horatmax  = dato_temperaturas["hora_maxima"]

        #Si alguno de los valores de las temperaturas viene como None, se ignora la lectura
        if tmin and tmax:
            #Se obtiene el indice (si existe) para una determinada provincia y fecha en la lista que se crea en esta función
            indice = next((index for (index, dato) in enumerate(datos_minimas_maximas_temperaturas) \
                        if dato["provincia"] == provincia and dato["fecha"] == fecha), None)

            #No hay entradas para la provincia y fecha que se esta procesando
            if not indice:
                #Se crea un diccionario para añadirlo posteriormente a la lista que se esta creando en la función
                registro_temperaturas = {
                        "provincia":   provincia,
                        "fecha":       fecha,
                        "minima":      tmin,
                        "hora_minima": horatmin,
                        "maxima":      tmax,
                        "hora_maxima": horatmax
                    }

                datos_minimas_maximas_temperaturas.append(registro_temperaturas)
            else:
                #Se ha enconrrado una entrada para esa provincia y fecha
                #print(indice, provincia, fecha, tmin, datos_minimas_maximas_temperaturas[indice]["minima"], tmax, datos_minimas_maximas_temperaturas[indice]["maxima"] )
                #Si la temperatura mímina es menor que la guardada, se almacena esta junto con su hora de toma
                if tmin < datos_minimas_maximas_temperaturas[indice]["minima"]:
                    datos_minimas_maximas_temperaturas[indice]["minima"]      = tmin
                    datos_minimas_maximas_temperaturas[indice]["hora_minima"] = horatmin

                #Si la temperatura máxima es mayor que la guardada, se almacena esta junto con su hora de toma
                if tmax > datos_minimas_maximas_temperaturas[indice]["maxima"]:
                    datos_minimas_maximas_temperaturas[indice]["maxima"]      = tmax
                    datos_minimas_maximas_temperaturas[indice]["hora_maxima"] = horatmax

    #Se retorna la lista que se ha creado ordenada por provincia y fecha
    return sorted(datos_minimas_maximas_temperaturas, key=lambda k: (k["provincia"], k["fecha"]))




### -------------------------------------------------- mostrar_datos_minimas_maximas_temperaturas() -------------------------------------------------- ###
#Mostrar los valores de termperaturas mínimas y máximas por provincia y día
def mostrar_datos_minimas_maximas_temperaturas(datos_minimas_maximas_temperaturas):
    for dato_minimas_maximas_temperaturas in datos_minimas_maximas_temperaturas:
        #print(dato_minimas_maximas_temperaturas)
        print("Provincia: {:20} Fecha: {} Mínima: {:>5} HoraMin: {:10} Máxima: {:>5} HoraMax: {:10}".format( \
            dato_minimas_maximas_temperaturas["provincia"], \
            dato_minimas_maximas_temperaturas["fecha"], \
            dato_minimas_maximas_temperaturas["minima"], \
            dato_minimas_maximas_temperaturas["hora_minima"], \
            dato_minimas_maximas_temperaturas["maxima"], \
            dato_minimas_maximas_temperaturas["hora_maxima"]))






##########################################################################################
#                                                                                        #
#                                                                                        #
#                                      M  A  I  N                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################
#Llamar a función main
if __name__ == "__main__":
    main()  