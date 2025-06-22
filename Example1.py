import random
import time
from BinarySearch import binarySearch
from LinearSearch import linearSearch
from InsertionSort import insertionsort
from QuickSort import quicksort
from BubbleSort import bubblesort

def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

n = 1000
lista_original = random.sample(range(1, n * 10), n)
objetivo = lista_original[n // 2]

print("Objetivo:", objetivo)
print("-" * 50)

lista_quick = lista_original.copy()
ordenada_quick, tiempo = medir_tiempo(quicksort, lista_quick)
print(f"QuickSort → {tiempo:.6f} s")

lista_insertion = lista_original.copy()
_, tiempo = medir_tiempo(insertionsort, lista_insertion)
print(f"InsertionSort → {tiempo:.6f} s")

lista_bubble = lista_original.copy()
_, tiempo = medir_tiempo(bubblesort, lista_bubble)
print(f"BubbleSort → {tiempo:.6f} s")

print("-" * 50)

_, tiempo = medir_tiempo(linearSearch, lista_original, objetivo)
print(f"Linear Search → {tiempo:.6f} s")

_, tiempo = medir_tiempo(binarySearch, ordenada_quick, objetivo)
print(f"Binary Search → {tiempo:.6f} s")



