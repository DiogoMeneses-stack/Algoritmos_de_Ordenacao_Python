from random import randrange
import random

#quick sort
def quicksort(lista, inicio=0, fim=None): #funcao
    if fim is None: #se fim é igual a null
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <=pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

#insertion sort
def insertion_sort(lista):
        n= len (lista)
        for i in range(1, n):
            chave = lista[i]
            j = i - 1
            while  j >= 0 and lista[j] > chave:
                lista[j+1] = lista[j]
                j = j - 1
            lista[j+1] = chave

#bubble sort
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n - 1):
            if lista[i] > lista[i+1]:
                #troca das posiçoes de i para i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]

#selection sort
def selection_sort(lista):
    n= len(lista)
    for j in range(n):
        min_index = 0
        for i in range(n):
            if lista[i] < min_index:
                min_index = i
        if list[j] < list[min_index]:
            aux = list[j]
            list[j] = list[min_index]
            list[min_index] = aux

#merge sort
def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

# Radix sort 
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    
#gnome sort
def gnomeSort(alist):
    for pos in range(1, len(alist)):
        while (pos != 0 and alist[pos] < alist[pos - 1]):
            alist[pos], alist[pos - 1] = alist[pos - 1], alist[pos]
            pos = pos - 1

#bogo sort
def bogoSort(a):
    n = len(a)
    while (is_sorted(a)== False):
        shuffle(a)
 
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]