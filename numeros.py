numero = 0
sumatorio = 0
mayor = 0
menor = 0
contador = 2
media = 0
cantidadDeElementos = 3

numero = int(input("Introducir número: "))

sumatorio += numero
mayor = menor = numero

while contador <= cantidadDeElementos:

  numero = int(input("Introducir número: "))

  if(numero > mayor):
    mayor = numero

  if(numero < menor):
    menor = numero

  sumatorio += numero

  contador += 1

media = sumatorio / cantidadDeElementos

print("Mayor: " + str(mayor))
print("Menor: " + str(menor))
print("Media: " + str(media))