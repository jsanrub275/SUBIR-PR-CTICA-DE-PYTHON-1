from aemet import Aemet, Estacion
import json
import datetime

AEMET_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhMjBzYW5ydWJqMDQzM0BpZXMtbWFyZGVjYWRpei5jb20iLCJqdGkiOiIxZGNhMjhmYS02MWFhLTQ2YTEtYWM5NS1kMTM5NWRjMDc1YjYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTYxMDcwNTU5NiwidXNlcklkIjoiMWRjYTI4ZmEtNjFhYS00NmExLWFjOTUtZDEzOTVkYzA3NWI2Iiwicm9sZSI6IiJ9.mAsykwB_ERJXD6L2MY6N4OnBkpMxV7GbS5oMHaQncnw"
ANDALUCIA = ("CADIZ", "HUELVA", "SEVILLA", "CORDOBA", "GRANADA", "MALAGA", "JAEN", "ALMERIA")

FECHA_INICIO = "2021-01-01"
FECHA_FIN    = "2021-01-15"

"""
aemet = Aemet(api_key=AEMET_API_KEY)
estaciones = Estacion.get_estaciones(AEMET_API_KEY)[:1]
datos = []
anyo_inicio, anyo_fin = 2016, 2017 + 1


for estacion in estaciones:
    print('{}: {}'.format(estacion['indicativo'], estacion['nombre']))
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

datos = []
anyo_inicio, anyo_fin = 2016, 2017 + 1

fecha_inicio = FECHA_INICIO + "T00:00:00UTC"
fecha_fin    = FECHA_FIN + "T23:59:59UTC"

aemet = Aemet(AEMET_API_KEY)

estaciones = Estacion.get_estaciones(AEMET_API_KEY)#[:10]




for estacion in estaciones:
    #if estacion["provincia"] in ANDALUCIA
    if estacion["provincia"] in ("CADIZ"): #in ANDALUCIA
        #print(estacion)
        #print("Provincia: {} Indicativo: {} Nombre: {}".format(estacion["provincia"], \estacion["indicativo"], estacion["nombre"]))
        valores_climatologicos_diarios = aemet.get_valores_climatologicos_diarios(fecha_inicio, fecha_fin, estacion["indicativo"])
        for valor_climatologico_diario in valores_climatologicos_diarios:
            #print(type(valor_climatologico_diario["tmin"]))
            print("Provincia: {:10} Nombre: {:40} Fecha: {} Mínima{:>5} HoraMin: {} Máxima: {:>5} HoraMax: {}".format(estacion["provincia"], \
                estacion["nombre"],  valor_climatologico_diario["fecha"], \
                valor_climatologico_diario["tmin"], valor_climatologico_diario["horatmin"], \
                valor_climatologico_diario["tmax"], valor_climatologico_diario["horatmax"]  ))

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
