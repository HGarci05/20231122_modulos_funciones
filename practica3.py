def obtener_numeros_pares(inicial, final):
    try:
        inicial = int(inicial)
        final = int(final)

        if inicial % 2 != 0:
            inicial += 1  # Ajusta el número inicial si es impar para comenzar con un número par

        numeros_pares = [num for num in range(inicial, final + 1, 2)]

        if numeros_pares:
            print(f"Números pares entre {inicial} y {final}: {numeros_pares}")
        else:
            print(f"No hay números pares en el rango especificado.")

    except ValueError:
        print("Error: Debes introducir valores numéricos para el número inicial y final.")
        obtener_numeros_pares(input("Introduce el número inicial: "), input("Introduce el número final: "))

if __name__ == "__main__":
    obtener_numeros_pares(input("Introduce el número inicial: "), input("Introduce el número final: "))
