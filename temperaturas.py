"""
get_valores_climatologicos_diarios(self, fechaini, fechafin, estacion, raw=False)
 |      Devuelve un diccionario con la información de todas las estaciones
 |      :param fechaini: Fecha inicio consulta
 |      :param fechafin: Fecha fin consulta
 |      :param estacion: ID de estación de IDEMA
 |      :param raw: [Opcional] Devuelve el resultado en formato json

5973

get_fecha_hoy(self)
 |      Devuelve la fecha formateada en el formato que acepta AEMET
2021-01-15 12:16:16.163703
return '{:%Y-%m-%d}'.format(datetime.now())
(AAAA-MM-DDTHH:MM:SSUTC)
2021-01-01T00:00:00UTC


https://github.com/pablo-moreno/python-aemet/blob/master/aemet/models.py
https://opendata.aemet.es/centrodedescargas/productosAEMET?
https://opendata.aemet.es/dist/index.html?#!/valores-climatologicos/Climatolog%C3%ADas_diarias
"""

#Importar sólo las clases del modulo de AEMET que se van a utilizar
from aemet import Aemet, Estacion
import json
import datetime 

#Constantes para la API_KEY de AEMET y para las provincias de Andalucía
AEMET_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhMjBzYW5ydWJqMDQzM0BpZXMtbWFyZGVjYWRpei5jb20iLCJqdGkiOiIxZGNhMjhmYS02MWFhLTQ2YTEtYWM5NS1kMTM5NWRjMDc1YjYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTYxMDcwNTU5NiwidXNlcklkIjoiMWRjYTI4ZmEtNjFhYS00NmExLWFjOTUtZDEzOTVkYzA3NWI2Iiwicm9sZSI6IiJ9.mAsykwB_ERJXD6L2MY6N4OnBkpMxV7GbS5oMHaQncnw"
ANDALUCIA = ("CADIZ", "HUELVA", "SEVILLA", "CORDOBA", "GRANADA", "MALAGA", "JAEN", "ALMERIA")

#Constantes para el rango de fechas a consultar de la API de la AEMET
FECHA_INICIO = "2021-01-07"
FECHA_FIN    = "2021-01-07"
#FECHA_FIN = str(datetime.datetime.now())[:10]

#datos = []
#anyo_inicio, anyo_fin = 2016, 2017 + 1

#Variables necesarias para consultar la API (No se cómo crear un datetime con el formato "AAAA-MM-DDTHH:MM:SSUTC")
fecha_inicio = FECHA_INICIO + "T00:00:00UTC"
fecha_fin    = FECHA_FIN + "T23:59:59UTC"

datos = []

#Se instancia la clase Aemet, pasándole la API
aemet = Aemet(AEMET_API_KEY)

#Se consultan todas las estaciones para poder recorrerlas posteriormente,
#ya que para obtener las valores climatológicos diarios es necesario el indicativo de la estación
estaciones = Estacion.get_estaciones(AEMET_API_KEY) #[:10]

#Se recorren las estaciones
for estacion in estaciones:
    #Sólo se toman las que nos interesan
    #if estacion["provincia"] in ANDALUCIA
    if estacion["provincia"] in ("CADIZ"):
        #print(estacion)
        #print("Provincia: {} Indicativo: {} Nombre: {}".format(estacion["provincia"], \estacion["indicativo"], estacion["nombre"]))
        valores_climatologicos_diarios = aemet.get_valores_climatologicos_diarios(fecha_inicio, fecha_fin, estacion["indicativo"])
        for valor_climatologico_diario in valores_climatologicos_diarios:
            print("Provincia: {:10} Nombre: {:40} Fecha: {} Mínima{:>5} HoraMin: {:10} Máxima: {:>5} HoraMax: {:10}".format(estacion["provincia"], \
                estacion["nombre"],  valor_climatologico_diario["fecha"], \
                valor_climatologico_diario["tmin"], valor_climatologico_diario["horatmin"], \
                valor_climatologico_diario["tmax"], valor_climatologico_diario["horatmax"]  ))

            registro = {
                "provincia": estacion["provincia"],
                "nombre": estacion["nombre"],
                "fecha": valor_climatologico_diario["fecha"],
                "minima": valor_climatologico_diario["tmin"],
                "hora_minima": valor_climatologico_diario["horatmin"],
                "maxima": valor_climatologico_diario["tmax"],
                "hora_maxima": valor_climatologico_diario["horatmax"]
            }

            datos.append(registro)

print(json.dumps(datos, indent=2))
"""
        for anyo in range(anyo_inicio, anyo_fin):
            vcm = aemet.get_valores_climatologicos_mensuales(anyo, estacion['indicativo'])
            resultado = {
                'estacion': estacion,
                'valores_climatologicos': vcm,
                'anyo': anyo
            }

            datos.append(resultado)

print(json.dumps(datos, indent=2))
"""




#print(aemet.get_valores_climatologicos_diarios("2021-01-01T00:00:00UTC", "2021-01-01T23:59:59UTC", "5911A"))
#print(aemet.get_valores_climatologicos_diarios("2021-01-01T00:00:00UTC", "2021-01-01T23:59:59UTC", "5973"))

#print(aemet.get_valores_climatologicos_diarios(fecha_inicio, fecha_fin, "5911A"))
#print(aemet.get_valores_climatologicos_diarios(fecha_inicio, fecha_fin, "5973"))
