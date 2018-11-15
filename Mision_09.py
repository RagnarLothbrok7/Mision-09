# Autor: Oscar Macias Rodríguez, A01376398.
# Descripción: Listas (Segunda Parte).


# Recibe como parámetro una lista de números enteros y regresa una lista nueva conteniendo los valores pares de la original.
def extraerPares(lista):
    nuevaLista = []

    for k in lista:
        if k % 2 == 0:
            nuevaLista.append(k)

    return nuevaLista


# Recibe como parámetro una lista y regresa una nueva lista con los valores que son mayores al previo.
def extraerMayoresPrevio(lista):
    nuevaLista = []

    for k in range(0, len(lista)-1):
        if lista[k+1] > lista[k]:
            nuevaLista.append(lista[k+1])

    return nuevaLista


# Recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiada.
def intercambiarParejas(lista):
    nuevaLista = []
    for parejas in range(1, len(lista), 2):
        nuevaLista.append(lista[parejas])
        nuevaLista.append(lista[parejas - 1])
    if len(lista) % 2 == 1:
        nuevaLista.append(lista[-1])
    return nuevaLista


# Recibe una lista de valores e intercambia el menor por el mayor.
def intercambiarMM(lista):

    if len(lista) == 0:
        pass
    else:
        mayor = list.index(lista, max(lista))
        menor = list.index(lista, min(lista))
        lista[mayor], lista[menor] = lista[menor], lista[mayor]

    return lista


# Recibe una lista y regresa el promedio entero de la lista sin considerar el mayor y el menor de los datos.
def promediarCentro(lista):
    nuevaLista = lista

    for n in nuevaLista:
        if len(nuevaLista) > 2:
            nuevaLista.pop(nuevaLista.index(max(nuevaLista)))
            nuevaLista.pop(nuevaLista.index(min(nuevaLista)))

            suma = 0

            for k in nuevaLista:
                suma += k

            promedio = suma / len(nuevaLista)

            return promedio

    return []


# Recibe una lista de números y regresa una dupla con la media y la desviación estándar.
def calcularEstadistica(lista):
    acumulador = 0
    if len(lista) > 0:
        media = sum(lista) / len(lista)
    else:
        media = 0
    if len(lista) > 1:
        for n in lista:
            acumulador += (n - media) ** 2
        deviation = (acumulador / (len(lista) - 1)) ** 0.5
    else:
        deviation = 0
    return media, deviation


# Recibe una lista y regresa la suma de la lista. Excepto los que están al lado de un número 13.
def calcularSuma(lista):
    nuevaLista = lista.copy()
    if 13 not in nuevaLista:
        return sum(nuevaLista)
    else:
        for n in range(len(nuevaLista)):
            if nuevaLista[n] == 13:
                if n != 0:
                    nuevaLista[n - 1] = 0
                if n != len(nuevaLista) - 1:
                    nuevaLista[n + 1] = 0
                    nuevaLista[n] = 0
    suma = sum(nuevaLista)
    return suma


# Prueba las funciones.
def main():
    print("Problema1: Regresa una lista con los valores pares de la lista original.")
    listaA = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaB = [3, 5, 7]
    listaC = []
    print("Con la lista", listaA, "regresa", extraerPares(listaA))
    print("Con la lista", listaB, "regresa", extraerPares(listaB))
    print("Con la lista", listaC, "regresa", extraerPares(listaC))
    print()

    print("Problema2: Regresa una lista con los valores que son mayores a un elemento previo.")
    listaD = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaE = [3, 5, 7, 9, 1]
    listaF = [7]
    print("Con la lista", listaD, "regresa", extraerMayoresPrevio(listaD))
    print("Con la lista", listaE, "regresa", extraerMayoresPrevio(listaE))
    print("Con la lista", listaF, "regresa", extraerMayoresPrevio(listaF))
    print()

    print("Problema3: Regresa una lista con cada pareja de datos intercambiada.")
    lista1 = [1, 2, 3, 4, 101, 1]
    lista2 = [3, 5, 7, 9, 1]
    lista3 = [7]
    print("Con la lista", lista1, "regresa", intercambiarParejas(lista1))
    print("Con la lista", lista2, "regresa", intercambiarParejas(lista2))
    print("Con la lista", lista3, "regresa", intercambiarParejas(lista3))
    print()

    print("Problema4: Intercambia el valor menor y mayor de una lista.")
    listaG = [5, 9, 3, 22, 19, 31, 10, 7]
    listaH = [1, 2, 3]
    listaI = []
    print("Con la lista", listaG, "regresa", intercambiarMM(listaG))
    print("Con la lista", listaH, "regresa", intercambiarMM(listaH))
    print("Con la lista", listaI, "regresa", intercambiarMM(listaI))
    print()

    print("Problema5: Promedia la lista sin considerar el máximo y el mínimo número.")
    listaJ = [5, 9, 3, 22, 19, 31, 10, 7]
    listaK = [1, 2, 4, 3]
    listaL = [1, 2]
    listaM = [1]
    listaN = []
    print("Con la lista", listaJ, "regresa", promediarCentro(listaJ))
    print("Con la lista", listaK, "regresa", promediarCentro(listaK))
    print("Con la lista", listaL, "regresa", promediarCentro(listaL))
    print("Con la lista", listaM, "regresa", promediarCentro(listaM))
    print("Con la lista", listaN, "regresa", promediarCentro(listaN))
    print()

    print("Problema6: Obtiene los valores de la media y de la desviación estandar.")
    listaO = [5, 9, 3, 22, 19, 31, 10, 7]
    listaP = [1, 2, 4, 3]
    listaQ = [1, 2]
    listaR = [1]
    listaS = []
    print("Con la lista", listaO, "regresa", calcularEstadistica(listaO))
    print("Con la lista", listaP, "regresa", calcularEstadistica(listaP))
    print("Con la lista", listaQ, "regresa", calcularEstadistica(listaQ))
    print("Con la lista", listaR, "regresa", calcularEstadistica(listaR))
    print("Con la lista", listaS, "regresa", calcularEstadistica(listaS))
    print()

    print("Problema7: Suma la lista sin contar lo numero alrededor del trece ni el trece.")
    listaT = [5, 9, 3, 22, 13, 19, 31, 10, 7]
    listaU = [1, 2, 4, 3]
    listaV = [1, 2]
    listaX = [1]
    listaY = []
    print("Con la lista", listaT, "regresa", calcularSuma(listaT))
    print("Con la lista", listaU, "regresa", calcularSuma(listaU))
    print("Con la lista", listaV, "regresa", calcularSuma(listaV))
    print("Con la lista", listaX, "regresa", calcularSuma(listaX))
    print("Con la lista", listaY, "regresa", calcularSuma(listaY))
    print()


main()






