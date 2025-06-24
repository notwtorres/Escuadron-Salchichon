import random
import time
from BinarySearch import binarySearch
from LinearSearch import linearSearch
from InsertionSort import insertionsort
from QuickSort import quicksort
from BubbleSort import bubblesort
from Mergesort import mergeSort
from Quicksort2 import quicksort as quicksort_async
import asyncio

def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

async def medir_tiempo_async(funcion, *args):
    inicio = time.time()
    resultado = await funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

async def main():
    n = 1000
    lista_original = random.sample(range(1, n * 10), n)
    objetivo = lista_original[n // 2]

    tiempos = {}
    print("Objetivo:", objetivo)
    print("-" * 50)

    lista_quick_async = lista_original.copy()
    _, tiempo = await medir_tiempo_async(quicksort_async, lista_quick_async)
    print(f"QuickSort Async → {tiempo:.10f} s")

    lista_quick = lista_original.copy()
    ordenada_quick, tiempo = medir_tiempo(quicksort, lista_quick)
    print(f"QuickSort → {tiempo:.5f} s")

    lista_insertion = lista_original.copy()
    _, tiempo = medir_tiempo(insertionsort, lista_insertion)
    print(f"InsertionSort → {tiempo:.5f} s")

    lista_bubble = lista_original.copy()
    _, tiempo = medir_tiempo(bubblesort, lista_bubble)
    print(f"BubbleSort → {tiempo:.5f} s")

    lista_merge = lista_original.copy()
    _, tiempo = medir_tiempo(mergeSort, lista_merge)
    print(f"MergeSort → {tiempo:.5f} s")

    print("-" * 50)

    _, tiempo = medir_tiempo(linearSearch, lista_original, objetivo)
    print(f"Linear Search → {tiempo:.5f} s")

    _, tiempo = medir_tiempo(binarySearch, ordenada_quick, objetivo)
    print(f"Binary Search → {tiempo:.5f} s")

if __name__ == "__main__":
    asyncio.run(main()) 