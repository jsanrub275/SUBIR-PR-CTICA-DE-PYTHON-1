#Importar sólo las clases del modulo de AEMET que se van a utilizar
from aemet import Aemet, Estacion
import json
import datetime 

#Constantes para la API_KEY de AEMET y para las provincias de Andalucía
AEMET_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhMjBzYW5ydWJqMDQzM0BpZXMtbWFyZGVjYWRpei5jb20iLCJqdGkiOiIxZGNhMjhmYS02MWFhLTQ2YTEtYWM5NS1kMTM5NWRjMDc1YjYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTYxMDcwNTU5NiwidXNlcklkIjoiMWRjYTI4ZmEtNjFhYS00NmExLWFjOTUtZDEzOTVkYzA3NWI2Iiwicm9sZSI6IiJ9.mAsykwB_ERJXD6L2MY6N4OnBkpMxV7GbS5oMHaQncnw"
#ANDALUCIA = ("CADIZ", "HUELVA", "SEVILLA", "CORDOBA", "GRANADA", "MALAGA", "JAEN", "ALMERIA")
ANDALUCIA = ("CADIZ", "HUELVA", "SEVILLA")

#Constantes para el rango de fechas a consultar de la API de la AEMET
FECHA_INICIO = "2021-01-01"
FECHA_FIN    = "2021-01-15"
#FECHA_FIN = str(datetime.datetime.now())[:10]



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
    estaciones = Estacion.get_estaciones(AEMET_API_KEY) #[:10]

    #Se recorren las estaciones
    for estacion in estaciones:
        #Sólo se toman las que nos interesan
        if estacion["provincia"] in ANDALUCIA:
            #print(estacion)
            #print("Provincia: {} Indicativo: {} Nombre: {}".format(estacion["provincia"], \estacion["indicativo"], estacion["nombre"]))
            valores_climatologicos_diarios = aemet.get_valores_climatologicos_diarios(fecha_inicio, fecha_fin, estacion["indicativo"])
            #print(valores_climatologicos_diarios)
            # {'descripcion': 'No hay datos que satisfagan esos criterios', 'estado': 404}

            #No hay datos para para esa estación en el rango de fechas que se ha pasado
            if isinstance(valores_climatologicos_diarios, dict) and "estado" in valores_climatologicos_diarios:
                """
                print("Descripción: {} - Estado: {}".format(\
                    valores_climatologicos_diarios["descripcion"], \
                    valores_climatologicos_diarios["estado"]))
                """
                pass
            else:
                #Recorrer lista para coger de cada entrada los valores que interesan
                for valor_climatologico_diario in valores_climatologicos_diarios:
                    #mostrar_datos_estacion_dia(estacion, valor_climatologico_diario)

                    datos_temperaturas.append(obtener_registro_temperaturas(estacion, valor_climatologico_diario, datos_temperaturas))

    #Una vez se tienen todos los datos de las estaciones, se muestran o se salvan
    if not datos_temperaturas:
        print("No hay datos para NINGUNA estación entre las fechas {} y {}.".format(FECHA_INICIO, FECHA_FIN))
    else:
        #print(json.dumps(datos_temperaturas, ensure_ascii=False, indent=2)).encode("utf8")

        with open("datos_temperaturas", "w", encoding="utf-8") as fichero:
            json.dump(datos_temperaturas, fichero, ensure_ascii=False, indent=4)




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
    print("Provincia: {:10} Nombre: {:40} Fecha: {} Mínima{:>5} HoraMin: {:10} Máxima: {:>5} HoraMax: {:10}".format(\
        estacion["provincia"], \
        estacion["nombre"],  \
        valor_climatologico_diario["fecha"], \
        valor_climatologico_diario["tmin"], \
        valor_climatologico_diario["horatmin"], \
        valor_climatologico_diario["tmax"], \
        valor_climatologico_diario["horatmax"]  ))






#Llamar a función main
if __name__ == "__main__":
    main()  