from datetime import datetime

time = datetime.now()

def flip(s, k):
    if k == 1:
        return s
    else:
        return s[:k][::-1] + s[k:]

def pancakes(arr):
    print(arr)
    flips = []
    n = len(arr)
    while n > 0:
        max_index = arr.index(n)
        if max_index != n-1: # si no esta en su lugar toca moverlo
            if max_index!=0: # si no esta en la primera posición toca ponerlo en la primera para luego ponerlo en la ultima
                print("flip en", max_index+1, "para poner", n, "en la primera posición")
                flips.append(max_index+1)
                arr = flip(arr, max_index+1)
                print(arr)
            print("flip en", n, "para acomodar")
            flips.append(n)
            arr = flip(arr, n) # se pone en la última posición
            print(arr)
            print("\n")
        n -= 1

        for i in range(n, 0, -1): # se buscan los siguientes elementos para saber si están ordenados
            if arr[n-1] == n:
                print(n, "está ordenado")
                n-=1
            else:
                break

    return flips


def main():
    arr = [2, 3, 1]
    flips = pancakes(arr)

    print("# de flips en cada posición: ")
    for i in range(1, len(arr)+1):
        print(i, ":", flips.count(i))


main()

print("Tiempo total:", datetime.now() - time)
