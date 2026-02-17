### Juan José Muñoz Jurado ###

# Simulador de "Pincho" de tickets Pila
tickets = []

print("--- COCINA ---")

# 1. PUSH: El cocinero termina platos y clava los tickets
tickets.append("Ticket #1: Hamburguesa") # Base
tickets.append("Ticket #2: Papas Fritas")
tickets.append("Ticket #3: Malteada")  # Cima

print(f"Tickets en la barra actualmente: {len(tickets)}")

# 2. PEEK: El mesero mira qué es lo último que salió sin quitarlo
if tickets:
    print(f"Mesero mira la barra: El último plato listo es '{tickets[-1]}'")

print("-" * 40)

# 3. POP: El repartidor llega y se lleva los pedidos
while len(tickets) > 0:
    # Sacamos el que está arriba
    pedido_entregado = tickets.pop()
    print(f"Repartidor se lleva: {pedido_entregado}")
    
    # 4. isEmpty: Verificamos si aún queda trabajo
    if not tickets:
        print("Cocina vacía! Todos los pedidos entregados.")
    else:
        print(f"Siguiente en la barra: {tickets[-1]}")