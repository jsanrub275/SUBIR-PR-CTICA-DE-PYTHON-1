"""Crear una matríz bidimensional de 7 x 8 y después de llenarla de números enteros, ordenarla de menor a mayor"""

#Función principal
def main():
    #Módulo para poder generar números pseudoaleatorio
    from random import randint

    #Definir el número de filas y columnas de la matriz bidimensional
    filas = 7
    columnas = 8

    #Definir el limite inferior y superior de valores para la generación de números pseudoaleatorios
    numero_minimo_random = 1
    numero_maximo_random = 9999

    #Generar una matriz bidimensional, en el que el número de filas y columnas se definan a través de variables 
    #Se genera un número pseudoaletorio para cada elmento que se crea
    matriz = [[randint(numero_minimo_random, numero_maximo_random) for j in range(columnas)] for i in range(filas)]

    #Se muestra el contenido de la mátriz antes de su ordenación
    print("\nAntes de ordenar:\n")
    dibujar_matriz(matriz)

    #Se ordena la matriz 
    ordenar_matriz(matriz, filas, columnas)
 
    #Se muestra el contenido de la mátriz después de su ordenación
    print("\nDespués de ordenar:\n")
    dibujar_matriz(matriz)



#Función para dibujar la matriz bidimensional en filas y columnas
def dibujar_matriz(matriz):
    #print('\n'.join(['\t'.join([str(columna) for columna in fila]) for fila in matriz]))
    for fila in matriz:
        for columna in fila:
            print("{:4d}  ".format(columna), end=" ")
        print()



#Función para ordenar la matriz bidimensional por el metodo de la burbuja
#La lista de dos dimensiones, al ser un objeto mutable, se está pasando por referencia 
# y por lo tanto se está modificando aqui directamente, con lo que no es necesario retornarlo
def ordenar_matriz(matriz, filas, columnas):
    #Se comparan todos con el siguiente y sólo se para cuando no se hace ningún intercambio
    hay_cambios = True
    while(hay_cambios):
        #Para cada recorrido, inicialmente vamos a definir que no se ha hecho ningún cambio
        hay_cambios = False
        
        #Se recorre cada fila (primera dimensión de la matriz)
        for i in range(filas):
            #Se recorre cada columna de cada fila (segunda dimensión de la matriz)
            for j in range(columnas):
                #Se ignora el intentar comparar el último elemento con un inexistente siguiente
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






#Llamar a función main
if __name__ == "__main__":
    main()
