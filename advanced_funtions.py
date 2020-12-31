#Función map
#map(funcion,secuencia)
#Ejecuta la función enviada por parámetro sobre cada uno de los elementos de la secuencia.

items = [1, 2, 3, 4, 5]
def cuadrado(x): 
    return x ** 2

print("Función map (cuadrado de cada elemento de la secuencia)")
print(items)
print(list(map(cuadrado, items)))

#Función filter 
#filter(funcion,secuencia)
#Devuelve una secuencia con los elementos de la secuencia envíada por parámetro 
#que devuelvan True al aplicarle la función envíada también como parámetro.

lista = [1,2,3,4,5]
def par(x): 
    return not(x % 2)

print()
print("Función filter (tomar sólo los elementos pares de la secuencia)")
print(lista)
print(list(filter(par,lista)))

#Función reduce
#reduce(funcion,secuencia)
#Devuelve un único valor que es el resultado de aplicar la función á los lementos de la secuencia.

from functools import reduce
lista = [1,2,3,4,5]
def add(x,y): 
    return x + y

print()
print("Función reduce (obtener la suma de los elementos de la secuencia)")
print(lista)
print(reduce(add,lista))

#List comprehension
#list comprehension 
#Nos propociona una alternativa para la creación de listas. 
#Es parecida a la función map, pero mientras map ejecuta una función por cada elemento de la secuencia, 
#con esta técnica se aplica una expresión.

print()
print("List comprehension")
print("Obtener el cubo de los elementos de una secuenciaS")
print("[x ** 3 for x in [1,2,3,4,5]])")
print([x ** 3 for x in [1,2,3,4,5]])

print()
print("Obtener sólo los elementos pares de una secuencia")
print("[x for x in range(11) if x % 2 == 0]")
print([x for x in range(11) if x % 2 == 0])

print()
print("Obtener la suma de los elementos de dos secuencias")
print("[x + y for x in [1,2,3] for y in [4,5,6]]")
print([x + y for x in [1,2,3] for y in [4,5,6]])
