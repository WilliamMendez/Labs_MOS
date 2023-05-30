"""
AUTORES:
Luis Felipe Torres
Daniel Felipe Vargas
"""
def flip(arr, k):
    return arr[:k] + arr[k:][::-1]

def pancakes(arr):
    flips = []
    n = len(arr) # n = tamaño del arreglo
    l = n # l = tamaño del arreglo
    while n > 0:

        max_index = arr.index(n) # max_index = indice del valor maximo
        if max_index != 0: # Si el valor maximo no esta en la primera posicion
            if max_index!=len(arr)-1: # Si el valor maximo no esta en la ultima posicion
                arr = flip(arr, max_index)
                flips.append(max_index)
            arr = flip(arr, len(arr)-n)
            flips.append(len(arr)-n)
        n -= 1

        for i in range(n, 0, -1):
            if arr[l-i] == n:
                n-=1
            else:
                break
    return flips

def main():
    n = int(input())
    for j in range(n):
        arr = [int(i) for i in input().split()]
        flips = pancakes(arr)
        if flips:
            flips = [str(x) for x in flips]
            print(" ".join(flips))
        else:
            print("ORDENADO")

main()