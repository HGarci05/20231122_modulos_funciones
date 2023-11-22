def suma_numeros():
    try:
        numeros = []

        while True:
            entrada = input("Introduce un número (o 'q' para salir): ")

            if entrada.lower() == 'q':
                break

            numero = float(entrada)
            numeros.append(numero)

        if len(numeros) == 0:
            print("No se introdujeron números.")
        else:
            resultado = sum(numeros)
            print(f"La suma de los números introducidos es: {resultado}")

    except ValueError:
        print("Error: Debes introducir un número válido.")
        suma_numeros()


if __name__ == "__main__":
    suma_numeros()
