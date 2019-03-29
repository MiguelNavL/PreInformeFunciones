#•	Una función que lea un número n imprima todos los números impares de 1 a n.

def impares (n):
    i=0
    for i in range (1,n):
        if i%2  != 0:
            print("el valor es: {}". format(i))

impares(9)

