# Inicializar variables
edadMayor = 0
edadMenor = 0
numeroEdadesPares = 0
numeroEdadesImpares = 0
NumeroPrimoMayor = 0

# Número de edades a solicitar
numeroEdadesASolicitar = 3

edad = 0


### F U N C I O N E S ###

# Función para ver si la edad es un número primo o no
def esNumeroPrimo(edad):
  # Un número es primo si SÓLO es divisible por si mismo y por la unidad
  # Tratamiento distinto del 1 y del resto
  if(edad == 1):
    esPrimo = False
  else:
    esPrimo = True

  # Obtener el primer posible divisor
  divisores = edad - 1

  # Recorrer todos los posibles divisores (menos el 1)
  while(divisores > 1):

    # En el momento que es divible por algún posible divisor, YA no es primo
    if(not(edad % divisores)):
      esPrimo = False
      break
    
    divisores -= 1

  # Retornar si esa edad es número primo o no
  return esPrimo



# Función para obtener el factorial del número
def ObtenerFactorial(NumeroPrimoMayor):
  factorial = 1

  while(NumeroPrimoMayor > 0):
    factorial *= NumeroPrimoMayor

    NumeroPrimoMayor -= 1

  return factorial



### M A I N ###

# Pedir la primera edad
edad = int(input("Introducir Edad: "))

# Inicializamos las edades mayor y menor con la primera leida
edadMayor = edadMenor = edad

# Ver si la edad leida es par o impar
if(edad % 2):
  numeroEdadesImpares += 1
else:
  numeroEdadesPares +=1

# Ver si la edad leida es un número primo
if(esNumeroPrimo(edad)):
  if(NumeroPrimoMayor < edad):
    NumeroPrimoMayor = edad



# Bucle para pedir N - 1 restantes edades
while(numeroEdadesASolicitar > 1):
  edad = int(input("Introducir Edad: "))

  # Ver si es la edad leida es mayor a la almacenada
  if(edad > edadMayor):
    edadMayor = edad

  # Ver si es la edad leida es menor a la almacenada
  if(edad < edadMenor):
    edadMenor = edad

  # Ver si la edad leida es par o impar
  if(edad % 2):
    numeroEdadesImpares += 1
  else:
    numeroEdadesPares +=1

  # Ver si la edad leida es un número primo
  if(esNumeroPrimo(edad)):
    if(edad > NumeroPrimoMayor):
      NumeroPrimoMayor = edad

  numeroEdadesASolicitar -= 1



# Mostrar resultados solicitados
print("Edad Mayor: " + str(edadMayor))
print("Edad Menor: " + str(edadMenor))
print("Numero de Edades Pares: " + str(numeroEdadesPares))
print("Numero de Edades Impares: " + str(numeroEdadesImpares))
if(NumeroPrimoMayor == 0):
  print("NO se ha introducido ninguna edad que sea número primo")
else:
  print("Edad número Primo Mayor: " + str(NumeroPrimoMayor))
  print ("Factorial del Número Primo: " + str(ObtenerFactorial(NumeroPrimoMayor)))