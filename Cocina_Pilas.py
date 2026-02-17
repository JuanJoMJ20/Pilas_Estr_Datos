### Juan José Muñoz Jurado ###
# Simulador de Barra de Pedidos (Estructura de Datos: Pila)

tickets = []

print("--- SISTEMA DE CONTROL DE BARRA ---")
print("Opciones: 1. Push (Agregar a la barra) | 2. Pop (Sacar de la barra) | 3. Peek (Ver cima) | 4. Salir")

while True:
    # Mostramos el estado de la barra para control del usuario
    print("\nEstado de la barra:", tickets)
    accion = input("Seleccione una operacion: ")

    if accion == "1":
        # Push (Empujar): Agregas un elemento a la cima de la pila.
        nuevo_ticket = input("Ingrese el nombre del plato: ")
        tickets.append(nuevo_ticket)
        print("Ticket agregado a la cima de la barra.")

    elif accion == "2":
        # isEmpty: Revisas si la pila esta vacia para evitar errores.
        if not tickets:
            print("Error: La barra esta vacia (isEmpty es True).")
        else:
            # Pop (Sacar): Eliminas el elemento que esta en la cima.
            pedido_entregado = tickets.pop()
            print("Sacando pedido de la cima:", pedido_entregado)

    elif accion == "3":
        # Peek/Top: Miras que hay en la cima sin quitar el elemento.
        if not tickets:
            print("La barra esta vacia, no hay nada en la cima.")
        else:
            print("Pedido en la cima de la barra (Peek):", tickets[-1])

    elif accion == "4":
        print("Finalizando sistema de barra.")
        break

    else:
        print("Opcion no valida.")