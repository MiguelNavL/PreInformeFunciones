#Una función que imprima el resultado de elevar un número a en b (es decir ab) sin utilizar la librería math.
# Hacer esta operación dos veces y comparar el primer resultado con el segundo, indicando cuál fue mayor.

def numero_a_elevar():

    numero = int(input("Digite un numero A: "))
    b = int(input("Digite un numero B: "))
    numero = numero**b
    print(numero)

numero_a_elevar()
numero_a_elevar()

