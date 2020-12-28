#Crear una matríz bidimensional de 7 x 8 y después de llenarla de números enteros, ordenarla de menor a mayor

#Módulo que implementar un generador de números pseudoaleatorio
import random

#Definir en variables el número de filas y columnas
filas = 7
columnas = 8

#Generar una matriz de "i" filas por "j" columnas
# matriz = [[i * j for j in range(columnas)] for i in range(filas)]
matriz = [[random.randint(1, 9999) for j in range(columnas)] for i in range(filas)]

#Se muestra el contenido de la mátriz antes de su ordenación
print("Antes de ordenar: ", matriz)

# Metodo de ordenación burbuja (se comparan todos con el siguiente y sólo se para cuando no se hace ningún intercambio)
hay_cambios = True
while(hay_cambios):
    hay_cambios = False
    
    for i in range(filas):
        for j in range(columnas):
            if(not(i == filas - 1 and j == columnas - 1)):
                #Definimos índices para el segundo elemento a comparar
                k = i
                l = j + 1

                #Si sobrepasa la última columna, cogemos el primer elemento de la siguiente fila 
                if(l == columnas):
                    k += 1
                    l = 0

                #Comparamos e intercambiamos si es mayor (y activamos flag)
                if(matriz[i][j] >  matriz[k][l]):
                    auxiliar = matriz[i][j]
                    matriz[i][j] = matriz[k][l]
                    matriz[k][l] = auxiliar

                    hay_cambios = True


#Se muestra el contenido de la mátriz después de su ordenación
print("Después de ordenar: ", matriz)

