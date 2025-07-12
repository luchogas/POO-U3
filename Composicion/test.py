from hotel import Hotel
from habitacion import Habitacion

def test():
    nombreHotel = input("Ingrese el nombre del hotel: ")
    h = Hotel(nombreHotel)
    
    res = input("¿Desea agregar habitaciones? (s/n): ")
    while res == 's':
        numero = int(input("Ingrese el número de la habitación: "))
        tipo = input("Ingrese el tipo de habitación (Individual, Doble, Suite, Familiar): ")
        capacidad = int(input("Ingrese la capacidad de la habitación: "))
        precio = float(input("Ingrese el precio por noche: "))
        disponible = input("¿Está disponible? (s/n): ").lower() == 's'
        h.agregarHabitacion(numero, tipo, capacidad, precio, disponible)
        res = input("¿Desea agregar otra habitación? (s/n): ").lower()

if __name__ == '__main__':
    test()
