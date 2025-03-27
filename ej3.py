def FibonacciSec(n):
    if n < 0:
        return "Error, Ingresar un numero positivo distinto de 0"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return FibonacciSec(n-1) + FibonacciSec(n-2)

if __name__=="__main__":
    n=int(input("Ingresar un numero entero positivo: "))

    if n < 0:
        print("Ingresar un numero positivo")
    else:
        print(f"El numero {n} en secuencia Fibonacci seria: {FibonacciSec(n)}")
    
    for i in range(n+1):
        print(FibonacciSec(i), end=" ")