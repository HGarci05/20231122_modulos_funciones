def sumar(i,j):
    return i+j
suma_anonima=lambda i,j:i+j
print(f'el total de la suma anonima es {suma_anonima}')
def sumar_default(i,j,k=15):
    return i+j+k
suma=sumar(4,5)
def sumar_variable(*args):
    total=0
    for i in args:
        total+=i
        return total
print(f'el total de la suma es {suma}')
suma2=sumar_default(4,5)
print(f'el total de la suma con argumentos={suma2}')
suma3=sumar_variable(5,9,4,7)
print(f'la suma total de una funcion con argumentos variable es {suma3}')
def factorial(n):
    if n==1:
        return
    elif n<=0:
        print('no hay numero factorial')
    else:
            return n+factorial (n-1)
    resultado_factoral=factorial(3)
    print(f'el factorial es {resultado_factoral}')