
def flip(s, k):
    if k == 1:
        return s
    else:
        return s[:k][::-1] + s[k:]

def pancakes(arr):
    print(arr)
    print("\n")
    flips = []
    n = len(arr)
    while n > 0:
        max_index = arr.index(n)
        if max_index != n-1: # si no está en su lugar toca moverlo
            if max_index!=0: # si no está en la primera posición toca ponerlo en la primera para luego ponerlo en la última
                print("flip en", max_index+1)
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
                n-=1
            else:
                break

    return flips


def main():
    arr = [int(i) for i in list(input("Ingrese el estado inicial: "))]
    flips = pancakes(arr)
    if flips:
        flips = [str(x) for x in flips]
        print(" ".join(flips))
        print("# de flips en cada posición: ")
        for i in range(1, len(arr)+1):
            print(i, ":", flips.count(str(i)))

    else:
        print("ORDENADO")


main()
