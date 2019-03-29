def primo(n):
    contador = 0
    i = 0
    for i in range (1,n+1):
        if (n%i)== 0:
            contador = contador + 1
    if contador == 2:
        print("el numero es primo")
    else:
        print("el numero no es primo")

primo(5)

