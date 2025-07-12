from gestorHotel import GestorHotel

def menu():
    print("\n--- MENÚ ---")
    print("1. Agregar habitación")
    print("2. Reservar habitación")
    print("3. Liberar habitación")
    print("4. Mostrar habitaciones por tipo")
    print("5. Mostrar cantidad de habitaciones libres por piso")
    print("6. Detalle por tipo de habitación")
    print("x. Salir")

if __name__ == '__main__':
    gestor = GestorHotel()
    gestor.cargar()
    op = ''
    while op != 'x':
        menu()
        op = input("Opción: ").lower()
        if op == '1':
            gestor.cargar()
        elif op == '2':
            num = int(input("Ingrese el número de habitación a reservar: "))
            gestor.reservarHabitacion(num)
        elif op == '3':
            num = int(input("Ingrese el número de habitación a liberar: "))
            gestor.liberarHabitacion(num)
        elif op == '4':
            tipoH = input("Ingrese el tipo de habitación a mostrar: ")
            gestor.mostrarPorTipo(tipoH)
        elif op == '5':
            gestor.libresPorPiso()
        elif op == '6':
            gestor.detallePorTipo()
        elif op == 'x':
            print("Saliendo...")
        else:
            print("Opción inválida")