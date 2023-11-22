def calcular_descuento(subtotal, dia_mes):
    # Si el día de hoy es anterior al 15 de cada mes, aplica un descuento del 5%
    if dia_mes < 15:
        descuento = subtotal * 0.05
        return descuento
    else:
        return 0


def calcular_total(unidades, precio, dia_mes):
    try:
        unidades = int(unidades)
        precio = float(precio)

        subtotal = unidades * precio
        descuento = calcular_descuento(subtotal, dia_mes)
        total = subtotal - descuento

        print(f"Subtotal: {subtotal}")
        print(f"Descuento aplicado: {descuento}")
        print(f"Total: {total}")

    except ValueError:
        print("Error: Debes introducir valores numéricos para unidades y precio.")
        calcular_total(input("Introduce las unidades: "), input("Introduce el precio: "), dia_mes)


if __name__ == "__main__":
    dia_mes = int(input("Introduce el día del mes: "))
    unidades = input("Introduce las unidades: ")
    precio = input("Introduce el precio: ")

    calcular_total(unidades, precio, dia_mes)

